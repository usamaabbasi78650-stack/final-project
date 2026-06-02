import React, { useState, useEffect } from 'react';

export default function Home() {
  const [services, setServices] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/services')
      .then(res => res.json())
      .then(data => setServices(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ fontFamily: 'Inter, sans-serif', padding: '20px', background: '#121212', color: '#fff', minHeight: '100vh' }}>
      <h1 style={{ fontSize: '2.5rem', color: '#4CAF50' }}>QuickServe</h1>
      <p>Smart Service & Utility Management System</p>
      
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))', gap: '20px', marginTop: '20px' }}>
        {services.length > 0 ? services.map(s => (
          <div key={s.id} style={{ padding: '20px', background: '#1e1e1e', borderRadius: '10px', boxShadow: '0 4px 6px rgba(0,0,0,0.3)' }}>
            <h3>{s.name}</h3>
            <p>{s.category}</p>
            <p style={{ color: '#4CAF50', fontWeight: 'bold' }}>${s.price}/hr</p>
            <button style={{ padding: '10px 15px', background: '#4CAF50', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>Book Now</button>
          </div>
        )) : <p>Loading services...</p>}
      </div>
    </div>
  );
}
