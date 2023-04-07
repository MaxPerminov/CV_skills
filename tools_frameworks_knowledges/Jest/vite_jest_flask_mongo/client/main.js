import "./style.css"
import {fd} from "./utils/fetchedData"

const btn_users = document.getElementById("get-users")
const btn_user = document.getElementById("get-user")
const people = document.getElementById("people")

btn_users.addEventListener("click",  async ()=> {
  const data = await fd("http://127.0.0.1:4321/", [])
    
  const domArr = data.map((el) => {
    return `
      <h2>
          name: ${el.name}
      </h2>

      <h2>
          age: ${el.age}
      </h2>

      <h2>
          hobby: ${el.hobby}
      </h2>    
    `
  })
  people.insertAdjacentHTML("afterend",domArr)
})

btn_user.addEventListener("click",  async ()=> {
  const data = await fd("http://127.0.0.1:4321/doc")
    
  const domDict = `<p>Their name is ${data.name}. They are ${data.age}. They like ${data.hobby}.</p>`  
  
  people.insertAdjacentHTML("afterend", domDict)
})
