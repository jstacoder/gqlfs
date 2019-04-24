import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import DirectoryRoot from './DirectoryRoot'

class Hello extends Component {
  render(){
    return (
      <DirectoryRoot  root={"c://Users//jstac//git//gql-fs"}/>
    )
  }
}

ReactDOM.render(<Hello />, document.getElementById("react"))
