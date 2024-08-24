import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [nudges, setNudges] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/api/nudges')
      .then(response => setNudges(response.data))
      .catch(error => console.error('Error fetching nudges:', error));
  }, []);

  return (
    <div>
      <h1>Nudge Engine</h1>
      <ul>
        {nudges.map((nudge, index) => (
          <li key={index}>{nudge.message}</li>
        ))}
      </ul>
    </div>
  );
}



export default App;
