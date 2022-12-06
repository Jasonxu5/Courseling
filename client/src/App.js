import React, { useState } from 'react'

const apiEndpoint = "http://localhost:5000/"

function App() {
  const [input, setInput] = useState('')

  const handleButtonClicked = async () => {
    let table = document.getElementById('table')
    table.innerHTML = null
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
    let courses = json.map(arr => arr[0])
    let scores = json.map(arr => arr[1])

    for (let i in courses) {
      let extTable = document.createElement("tr")
      let course = document.createElement("td")
      let score = document.createElement("td")


      course.textContent = courses[i]
      score.textContent = scores[i]
      // tr.insertCell().textContent = i
      extTable.append(course)
      extTable.append(score)
      parent.append(extTable)
    }

    console.log(parent)

    table.append(parent)
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