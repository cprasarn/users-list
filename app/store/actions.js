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
  async updateUser({commit, state}, user) {
    let user_data = {
      id: user.id,
      firstname: user.firstname,
      lastname: user.lastname,
      email: user.email,
      age: user.age,
      gender: user.gender
    }
    let {data} = await this.$axios.put(`/users/${user.id}`, user_data)
    commit('updateUsers', user_data)
  },
  async removeUser({commit, state}, user) {
    let {data} = await this.$axios.delete(`/users/${user.id}`)
    commit('setUsers', data)
  },
  async nuxtServerInit ({dispatch, commit}, {store, route, params}) {
    await dispatch('getUsers')
  }
}

export default actions
