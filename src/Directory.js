import React, { Component } from 'react'
import DirectoryItem from './DirectoryItem'


export default class Directory extends Component {

  setNewPath = path =>{
    console.log(path, this.props.currentPath)
    this.props.setPath(path, this.props.currentPath)
  }

  render() {

    return this.props.childItems && (
      <div>
    <h2>{this.props.name}</h2>
    <ul>
        {this.props.childItems.map(child => (
          <li style={{cursor: child.isDirName && 'pointer'}} key={child.name} onClick={()=>child.isDirName && this.setNewPath(child.path)}><DirectoryItem item={child}/></li>
        ))}
    </ul>
  </div>
    ) || null
  }
}
