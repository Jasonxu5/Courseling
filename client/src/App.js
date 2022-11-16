import React, { useState } from 'react'

const apiEndpoint = "http://localhost:5000/"

function App() {
  const [input, setInput] = useState('')
  const [html, set_html] = useState(null)

  const handleButtonClicked = async () => {
    let searchQuery = input

    let response = await fetch(apiEndpoint + `courses?query=${searchQuery}`);
    let json = await response.json()

    set_html(
      <div>
        <p>{json.description}</p>
      </div>
    )
  }

  return (
    <div>
      <label>Input an query:</label>
      <input type="text" value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={() => { handleButtonClicked() }}>Submit</button>
      {html}
    </div>
  )
}

export default App