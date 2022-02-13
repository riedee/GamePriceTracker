<template>
    <div @submit.prevent="submitSearch">
        <input type="text" v-model="game" placeholder="Search game">
        <button type="submit">Submit</button>
    </div>
</template>