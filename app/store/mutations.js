const mutations = {
  setUsers: (state, users) => {
    state.users = users
  },
  setCurrentUser: (state, user) => {
    state.current_user = user
  },
  addUser: (state, user) => {
    state.users.push(user);
  },
  removeUser: (state, user) => {
    state.users = state.users.filter(obj => obj.id != user.id);
  },
  updateUsers: (state, user) => {
    var index = state.users.findIndex(obj => obj.id == user.id);
    state.users.splice(index, 1, user);
  }
}

export default mutations
