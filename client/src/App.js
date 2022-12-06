import React, { useState } from 'react'

const apiEndpoint = "http://localhost:5000/"

function App() {
  const [input, setInput] = useState('')

  const handleButtonClicked = async () => {
    let searchQuery = input

    let response = await fetch(apiEndpoint + `courses?query=${searchQuery}`);
    let json = await response.json()

    console.log(json)

    let parent = document.createElement("table")
    let headers = document.createElement("tr")
    let classHeader = document.createElement("th")
    let scoreHeader = document.createElement("th")
    classHeader.textContent = "Class"
    scoreHeader.textContent = "Ranking Score"
    headers.append(classHeader)
    headers.append(scoreHeader)

    parent.append(headers)
    for (let i in json) {
      let extTable = document.createElement("tr")
      let course = document.createElement("td")
      let score = document.createElement("td")
      course.textContent = i
      score.textContent = json[i]
      // tr.insertCell().textContent = i
      extTable.append(course)
      extTable.append(score)
      parent.append(extTable)
    }

    console.log(parent)

    document.getElementById('table').append(parent);
  }

  return (
    <div>
      <label>Input an query:</label>
      <input type="text" value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={() => { handleButtonClicked() }}>Submit</button>
      <div id="table"></div>
    </div>
  )
}

export default App