import React, { useState } from 'react'
import "./styles.css"

const apiEndpoint = "http://localhost:5000/"

function App() {
  const [input, setInput] = useState('')
  const [html, set_html] = useState(null)
  const [result, set_result] = useState(null)

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
      extTable.append(course)
      extTable.append(score)
      parent.append(extTable)
    }

    console.log(parent)

    table.append(parent)
    displayCourseSearcher()
  }

  const handleCourseButtonClicked = async () => {
    let searchQuery = document.getElementById('search-box').value

    let response = await fetch(apiEndpoint + `search?query=${searchQuery}`)
    let json = await response.json()

    console.log(json)

    set_result(
      <div>
        <p>{json.description}</p>
      </div>
    )
  }

  function displayCourseSearcher() {
    set_html(
      <div id="search-area">
        <label>Search for a course:</label>
        <input id="search-box" type="text" size="30" />
        <button onClick={() => { handleCourseButtonClicked() }}>Search</button>
      </div>
    )
  }

  return (
    <div>
      <label>Input a query:</label>
      <input type="text" value={input} onChange={e => setInput(e.target.value)} size="30" />
      <button onClick={() => { handleButtonClicked() }}>Submit</button>
      <div id="table"></div>
      {html}
      {result}
    </div>
  )
}

export default App