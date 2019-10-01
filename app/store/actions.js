const actions = {
  async signup({commit, store}, signup) {
    let {data} = await this.$axios.post('/register', signup)
  },
  async getUsers({commit, store}, search) {
    let params = { s: search }
    let {data} = await this.$axios.get(`users`, { params: params })
    commit('setUsers', data)
  },
  async getCurrentUser({commit, store}, id) {
    let {data} = await this.$axios.get(`/users/${id}`)
    commit('setCurrentUser', data)
  },
  async addUser({commit, state}, user) {
    let {data} = await this.$axios.post('/register', user)
    user.id = data.id
    commit('addUser', user)
  },
  async updateUser({commit, state}, user) {
    let {data} = await this.$axios.put(`/users/${user.id}`, user)
    commit('updateUsers', user)
  },
  async removeUser({commit, state}, user) {
    let {data} = await this.$axios.delete(`/users/${user.id}`)
    commit('removeUser', user)
  },
  async nuxtServerInit ({dispatch, commit}, {store, route, params}) {
    await dispatch('getUsers')
  }
}

export default actions
