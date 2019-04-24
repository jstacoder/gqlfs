import React, { Component } from 'react'
import axios from 'axios'
import Directory from './Directory'
import GoToParent from './GoToParent'


const url = '/graphiql'

const query = 'query=query getDir($input: DirectoryInputType){getDirectory(directoryInput: $input){ name children { ...on Directory { name path isDirName:name } ...on File { name path } } } }'

const VARIABLE_TEMPLATE = `variables=${JSON.stringify()}`



class DirectoryRoot extends Component {
  state = {
    lastParent: null,
    parentPath: null,
    updating: false,
    data: {},
    variables: {input: {path: null}},
  }
  makeUrl = (queryVar, variables) => {
    const parsedVariables = `variables=${JSON.stringify(variables)}`
    return `${url}?${parsedVariables}&${queryVar}`
  }
  componentDidMount() {
    this.setVariables(
      this.props.root,
      this.props.root,
      async ()=> {
          await this.makeRequest(
            this.state.variables,
            this.makeUrl
          )
      }
    )
  }
  async makeRequest(variables, makeUrl){

        const res = await axios.get(
          makeUrl(
            query,
            variables
          )
        )
        this.setData(res.data.data.getDirectory)
  }

  componentDidUpdate(prevProps, prevState){
    if(prevState.updating != this.state.updating) {
      this.makeRequest(this.state.variables, this.makeUrl)
    }
  }

  setData = data =>{
    this.setState({data, updating: false})
  }

  setVariables = (path, root, cb) =>{

    this.setState((prevState, prevProps)=>{
      return {
        lastParent: prevState.parentPath,
        parentPath: root,
        updating: true,
        variables: {
          input: {
            path
          }
        }}
    }, cb)
  }

  render() {
        console.log(this.state.lastParent)
        const inRoot = this.state.variables &&
                          this.state.variables.input &&
                            this.state.variables.input.path === this.props.root
        return this.state.data != {} && (
	          <React.Fragment>
              {!inRoot && <GoToParent
                            setRoot={this.setVariables}
                            parent={this.state.parentPath}
                            oldParent={this.state.lastParent}
                            />}
	            <Directory
                setPath={this.setVariables}
                currentPath={this.state.variables.input.path}
                childItems={this.state.data.children}
                name={this.state.data.name} />
	          </React.Fragment>
	      )
    }
}

export default DirectoryRoot