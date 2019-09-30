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
    let user_data = {
      id: '',
      firstname: user.firstname,
      lastname: user.lastname,
      email: user.email,
      age: user.age,
      gender: user.gender
    }
    let {data} = await this.$axios.post('/register', user_data)
    user_data.id = data.id
    commit('addUser', user_data)
  },
  async removeUser({commit, state}, user) {
    let {data} = await this.$axios.post(`/delete`, { id: user.id })
    commit('removeUser', user)
  },
  async nuxtServerInit ({dispatch, commit}, {store, route, params}) {
    await dispatch('getUsers')
  }
}

export default actions
