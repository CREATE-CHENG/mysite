import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  user: {
    username: sessionStorage.getItem('user'),
    token: sessionStorage.getItem('token'),
    avatar: sessionStorage.getItem('avatar')
  }
}

const getters = {
  user: state => {
    return state.user
  }
}

const actions = {
  setuser ({ commit }) {
    commit('setuser')
  }
}

const mutations = {
  setuser (state) {
    state.user = {
      username: sessionStorage.getItem('user'),
      token: sessionStorage.getItem('token'),
      avatar: sessionStorage.getItem('avatar')
    }
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
