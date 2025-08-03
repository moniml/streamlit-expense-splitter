import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [members, setMembers] = useState([]);
  const [memberName, setMemberName] = useState('');
  const [expenses, setExpenses] = useState([]);
  const [payer, setPayer] = useState('');
  const [amount, setAmount] = useState('');
  const [participants, setParticipants] = useState('');
  const [currency, setCurrency] = useState('INR');

  const addMember = () => {
    if (memberName && !members.includes(memberName)) {
      setMembers([...members, memberName]);
      setMemberName('');
    }
  };

  const addExpense = () => {
    if (payer && amount && participants) {
      setExpenses([
        ...expenses,
        {
          payer,
          amount: parseFloat(amount),
          participants: participants.split(',').map((p) => p.trim())
        }
      ]);
      setPayer('');
      setAmount('');
      setParticipants('');
    }
  };

  const calculateSettlements = () => {
    const balances = {};
    members.forEach(m => (balances[m] = 0));

    for (let exp of expenses) {
      const share = exp.amount / exp.participants.length;
      for (let part of exp.participants) {
        if (part !== exp.payer) {
          balances[part] -= share;
          balances[exp.payer] += share;
        }
      }
    }

    const settlements = [];
    const debtors = Object.entries(balances).filter(([_, v]) => v < 0);
    const creditors = Object.entries(balances).filter(([_, v]) => v > 0);

    let i = 0, j = 0;
    while (i < debtors.length && j < creditors.length) {
      const [debtor, debtAmt] = debtors[i];
      const [creditor, creditAmt] = creditors[j];

      const amount = Math.min(-debtAmt, creditAmt);
      settlements.push(`${debtor} pays ${creditor}: ${amount.toFixed(2)} ${currency}`);

      debtors[i][1] += amount;
      creditors[j][1] -= amount;

      if (Math.abs(debtors[i][1]) < 0.01) i++;
      if (Math.abs(creditors[j][1]) < 0.01) j++;
    }

    return settlements;
  };

  return (
    <div className="container py-4">
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <div className="container-fluid">
          <span className="navbar-brand">Expense Splitter</span>
          <div className="d-flex">
            <label className="text-white me-2 mt-2">Currency:</label>
            <select
              className="form-select"
              style={{ width: '100px' }}
              value={currency}
              onChange={(e) => setCurrency(e.target.value)}
            >
              <option value="INR">INR</option>
              <option value="USD">USD</option>
              <option value="EUR">EUR</option>
            </select>
          </div>
        </div>
      </nav>

      {/* Member input */}
      <div className="mb-3">
        <h4>Add Members</h4>
        <div className="input-group mb-2">
          <input
            type="text"
            className="form-control"
            placeholder="Enter name"
            value={memberName}
            onChange={(e) => setMemberName(e.target.value)}
          />
          <button className="btn btn-success" onClick={addMember}>
            Add Member
          </button>
        </div>
        <div>
          <strong>Members:</strong> {members.length > 0 ? members.join(', ') : 'None'}
        </div>
      </div>

      {/* Expense input */}
      <div className="mb-3">
        <h4>Add Expenses</h4>
        <input
          type="text"
          className="form-control mb-2"
          placeholder="Payer name"
          value={payer}
          onChange={(e) => setPayer(e.target.value)}
        />
        <input
          type="number"
          className="form-control mb-2"
          placeholder="Amount paid"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
        <input
          type="text"
          className="form-control mb-2"
          placeholder="Participants (comma separated)"
          value={participants}
          onChange={(e) => setParticipants(e.target.value)}
        />
        <button className="btn btn-primary" onClick={addExpense}>
          Add Expense
        </button>
      </div>

      {/* Settlements */}
      <div className="mt-4">
        <h4>Settlement Suggestions</h4>
        <ul className="list-group">
          {calculateSettlements().map((s, index) => (
            <li className="list-group-item" key={index}>
              {s}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
