import axios from 'axios'

let host = 'http://127.0.0.1:8000'

export const getlist = params => { return axios.get(`${host}/api/articles/`, {params: params}) }
export const getcategories = () => { return axios.get(`${host}/api/categories/`) }
export const getarticle = articleid => { return axios.get(`${host}/api/articles/${articleid}/`) }
export const delarticle = articleid => { return axios.delete(`${host}/api/articles/${articleid}/`) }
export const getarchive = () => { return axios.get(`${host}/api/archive/`) }
export const getjwt = () => { return axios.get(`${host}/api/social_to_jwt/`) }
export const logout = () => { return axios.get(`${host}/api-auth/logout/`) }
export const checkpermission = () => { return axios.get(`${host}/api/check_permission/`) }
export const imageupload = params => { return axios.post(`${host}/api/images/`, params, {headers: { 'Content-Type': 'multipart/form-data' }}) }
export const imagedel = imageid => { return axios.delete(`${host}/api/images/${imageid}`) }
export const addcomment = params => { return axios.post(`${host}/api/comments/`, params) }
export const addarticle = params => { return axios.post(`${host}/api/articles/`, params) }
export const addcat = params => { return axios.post(`${host}/api/categories/`, params) }
export const updatecat = (id, params) => { return axios.patch(`${host}/api/categories/${id}/`, params) }
export const updatearticle = (id, params) => { return axios.patch(`${host}/api/articles/${id}/`, params) }
