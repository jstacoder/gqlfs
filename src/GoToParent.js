import React, { Component } from 'react'

class GoToParent extends Component {
  goToParent = () =>{
    console.log(this.props.parent, this.props.oldParent, this.props)
    this.props.setRoot(this.props.parent, this.props.oldParent)
  }

  render() {
    console.log(this.props.parent, this.props.oldParent, this.props)
    return (
      <div>
        <p
          onClick={this.goToParent}
          style={{fontSize: '2em', lineHeight: 0.5, cursor: 'pointer'}}>
            &#8592;
        </p>
      </div>
    )
  }
}

export default GoToParent