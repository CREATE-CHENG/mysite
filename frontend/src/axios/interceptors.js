import axios from 'axios'
import store from '../store/store'

axios.defaults.withCredentials = true

axios.interceptors.request.use(
  data => {
    if (store.state.user.token) {
      data.headers.Authorization = `JWT ${store.state.user.token}`
    }
    return data
  }
)
