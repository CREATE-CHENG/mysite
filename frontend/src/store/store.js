import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  user: {
    username: sessionStorage.getItem('user'),
    token: sessionStorage.getItem('token'),
    avatar: sessionStorage.getItem('avatar')
  },
  permission: 0
}

const getters = {
  user: state => {
    return state.user
  },
  permission: state => {
    return state.permission
  }
}

const actions = {
  setuser ({ commit }) {
    commit('setuser')
  },
  setpermission ({ commit, permission }) {
    commit('setpermission', permission)
  }
}

const mutations = {
  setuser (state) {
    state.user = {
      username: sessionStorage.getItem('user'),
      token: sessionStorage.getItem('token'),
      avatar: sessionStorage.getItem('avatar')
    }
  },
  setpermission (state, permission) {
    state.permission = permission
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
