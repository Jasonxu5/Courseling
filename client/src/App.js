// RUN python server.py then in another terminal npm start
// npm build and load unpacked in chrome extensions to run extension
// making into extensions doesnt work. how to make app.js rendering to a html?
import React, { useState, useEffect } from 'react'

function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("http://localhost:3000/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  return (
    <div>

      {(typeof data.members === 'undefined') ? (
        <p>Loading...</p>
      ) : (
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )}

    </div>
  )
}

export default App
