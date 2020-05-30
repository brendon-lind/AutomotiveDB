<template>
    <div>
        <v-card
            fluid
        >
            Car
            {{car.name}}
            {{car.customer_name}}
        </v-card>
        <v-card
            fluid
        >
            Comments

        </v-card>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                car: {},
            }
        },
        methods: {
            get_car() {
                try {
                    resp = this.$axios.get(`/api/cars/${this.$route.params.car_id}`)
                    this.car = resp.data
                    console.log(this.car)
                } catch {
                    console.log("Failed to get car.")
                }
            }
        },
        async mounted() {
            this.get_car()
        }
    }
</script>

<style scoped>

</style>
