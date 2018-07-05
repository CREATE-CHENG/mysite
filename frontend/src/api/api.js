import axios from 'axios'

let host = 'http://localhost:8000'

export const getlist = params => { return axios.get(`${host}/articles/`, {params: params}) }
export const getcategories = params => { return axios.get(`${host}/categories/`) }

