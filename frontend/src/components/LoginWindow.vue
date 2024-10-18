<template>
<div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
    <input
        v-model="username"
        type="text"
        placeholder="Enter your name"
        class="input-field"
    />
    <button type="submit" class="login-button">Login</button>
    </form>
</div>
</template>

<script>
export default {
data() {
    return {
    username: "",
    };
},
methods: {
    handleLogin() {
    if (this.username) {
        console.log(`Logging in as: ${this.username}`);
        // Handle the login logic here
    }
    },
},
};
</script>

<style scoped>
.login-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 300px;
    width: 200px;
    background-color: #f5f5f5;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-bottom: 20px;
    font-size: 1.5em;
    color: #333;
}

form {
    display: flex;
    flex-direction: column;
    width: 100%;
    align-items: center;
}

.input-field {
    width: 90%;
    padding: 8px;
    margin-bottom: 15px;
    border-radius: 5px;
    border: 1px solid #ccc;
}

.login-button {
    width: 90%;
    padding: 10px;
    background-color: #333;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.login-button:hover {
    background-color: #444;
}
</style>
