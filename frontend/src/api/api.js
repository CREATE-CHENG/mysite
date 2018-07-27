import axios from 'axios'

let host = 'http://127.0.0.1:8000'

export const getlist = params => { return axios.get(`${host}/api/articles/`, {params: params}) }
export const getcategories = params => { return axios.get(`${host}/api/categories/`) }
export const getarticle = articleid => { return axios.get(`${host}/api/articles/${articleid}/`) }
export const getarchive = params => { return axios.get(`${host}/api/archive/`) }
export const getjwt = params => { return axios.get(`${host}/social_to_jwt/`) }
export const logout = params => { return axios.get(`${host}/api-auth/logout/`) }
export const imageupload = params => { return axios.post(`${host}/api/image_upload/`, params, {headers: { 'Content-Type': 'multipart/form-data' }}) }
export const addcomment = params => { return axios.post(`${host}/api/comments/`, params) }
export const addarticle = params => { return axios.post(`${host}/api/articles/`, params) }
