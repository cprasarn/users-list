<template>
  <section class="section">
    <div class="container">
      <UsersList />
    </div>
  </section>
</template>

<script>
import UsersList from '~/components/users_list';

export default {
  components: {
    UsersList,
  }
}
</script>
