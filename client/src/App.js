import React, { useState } from 'react'

const apiEndpoint = "http://localhost:5000/"

function App() {
  const [input, setInput] = useState('')
  const [html, set_html] = useState(null)
  const [table, set_table] = useState(null)

  const handleButtonClicked = async () => {
    let searchQuery = input

    let response = await fetch(apiEndpoint + `courses?query=${searchQuery}`);
    let json = await response.json()

    console.log(json)

    let keys = Object.keys(json)
    console.log(keys)

    let extTable = document.createElement("tr")
    for (let i in keys) {
      let row = document.createElement("th")
      row.textContent = i
      // tr.insertCell().textContent = i
      extTable.append(row)
    }

    console.log(extTable)

    set_table(
      extTable
    )

    // set_html(
    //   <div>
    //     <p>{json.description}</p>
    //   </div>
    // )
  }

  return (
    <div>
      <label>Input an query:</label>
      <input type="text" value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={() => { handleButtonClicked() }}>Submit</button>
      {html}
      <table>
        <tr>
          <th>Class</th>
          <th>Ranking Score</th>
        </tr>
        {table}
      </table>
    </div>
  )
}

export default App