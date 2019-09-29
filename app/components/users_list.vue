<template>
  <div>
    <div class="container">
      <div class="search_box">
      </div>
      <div class="new_user">
        <b-btn v-b-modal.new_user_modal size="sm" class="float-right">
          New User
        </b-btn>
      </div>
      <b-table show-empty striped hover
             :sort-by.sync="sortBy"
             :sort-desc.sync="sortDesc"
             :items="users"
             :fields="fields">
        <template v-slot:cell(index)="data">
          {{ data.index + 1 }}
        </template>
        <template v-slot:cell(name)="data">
          {{ data.item.firstname }} {{ data.item.lastname }}
        </template>
        <template v-slot:cell(actions)="data">
          <b-btn v-b-modal.remove_user_modal 
            variant="danger"
            size="sm" 
            @click="setUser(data.item)">
              Remove
          </b-btn>
        </template>
      </b-table>
      <b-modal 
        id="new_user_modal"
        title="New User"
        @ok="newUser"
        @shown="clearUser">
        <b-container fluid>
          <b-row>
            <b-col sm="3"><label for="firstname">Name</label></b-col>
            <b-col sm="3">
              <b-form-input 
                v-model="user1.firstname"
                id="firstname"
                type="text"
                placeholder="Firstname">
              </b-form-input>
            </b-col>
            <b-col sm="3">
              <b-form-input 
                v-model="user1.lastname"
                id="lastname"
                type="text"
                placeholder="Lastname">
              </b-form-input>
            </b-col>
          </b-row>
          <b-row>
            <b-col sm="3"><label for="email">Email</label></b-col>
            <b-col sm="9">
              <b-form-input 
                v-model="user1.email"
                id="email"
                type="text"
                placeholder="Email">
              </b-form-input>
            </b-col>
          </b-row>
          <b-row>
            <b-col sm="3"><label for="age">Age</label></b-col>
            <b-col sm="3">
              <b-form-input 
                v-model="user1.age"
                id="age"
                type="text"
                placeholder="Age">
              </b-form-input>
            </b-col>
          </b-row>
          <b-row>
            <b-col sm="3"><label for="gender">Gender</label></b-col>
            <b-col sm="3">
              <b-form-input 
                v-model="user1.gender"
                id="gender"
                type="text"
                placeholder="Gender">
              </b-form-input>
            </b-col>
          </b-row>
        </b-container>
      </b-modal>
      <b-modal id="remove_user_modal"
               title="Confirm Removing User"
               @ok="deleteUser">
        <b-container fluid>
          <p>By clicking 'OK' button, the following user will be removed from the system.</p>
          <b-row>
            <b-col sm="3"><label>Name</label></b-col>
            <b-col sm="9"><label>{{ current_user.firstname }} {{ current_user.lastname }}</label></b-col>
          </b-row>
          <b-row>
            <b-col sm="3"><label>Email</label></b-col>
            <b-col sm="9"><label>{{ current_user.email }}</label></b-col>
          </b-row>
          <b-row>
            <b-col sm="3"><label>Age</label></b-col>
            <b-col sm="9"><label>{{ current_user.age }}</label></b-col>
          </b-row>
          <b-row>
            <b-col sm="3"><label>Gender</label></b-col>
            <b-col sm="9"><label>{{ current_user.gender }}</label></b-col>
          </b-row>
        </b-container>
      </b-modal>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "UsersList",

  data() {
    return {
      user1: {
        firstname: '',
        lastname: '',
        email: '',
        age: 0,
        gender: ''
      },
      sortBy: 'date_created',
      sortDesc: false,
      fields: [
        { key: 'index', label: '#' },
        { key: 'name', label: 'Name' },
        { key: 'email', label: 'Email', sortable: true },
        { key: 'age', sortable: true },
        { key: 'gender', label: 'Gender', sortable: true },
        { key: 'actions', label: 'Action' }
      ]
    }
  },

  computed: {
    ...mapState([
      'users',
      'current_user'
    ])
  },

  methods: {
    ...mapActions([
      'getCurrentUser',
      'addUser',
      'removeUser'
    ]),

    clearUser() {
      this.user1 = {
        firstname: '',
        lastname: '',
        email: '',
        age: 0,
        gender: ''
      };
    },

    newUser(evt) {
      this.$store.dispatch('addUser', this.user1);
    },

    setUser(user) {
      this.$store.dispatch('getCurrentUser', user.id);
    },

    deleteUser(evt) {
      this.$store.dispatch('removeUser', this.current_user);
    },

    showUser(u) {
      this.$store.dispatch(
        'getCurrentUser',
        u.id
      ).then(() => {
        this.$router.push({ name: 'users-id', params: { id: u.id } });
      });
    }
  }
}
</script>

<style scoped>
.new_property {
  padding: 10px 0;
}
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto;
  justify-content: space-between;
  grid-gap: 10px;
}
.flex-container {
  display: flex;
  flex-flow: row wrap;
  justify-content: space-between;
  align-content: space-around;
}
</style>
