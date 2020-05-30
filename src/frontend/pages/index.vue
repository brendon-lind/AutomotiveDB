<template>
    <div>
        <v-container>
            <v-row justify="center">
                <v-col cols="6">
                    <v-text-field
                        v-model="search"
                        append-icon="mdi-magnify"
                        label="Search"
                        solo
                        dense
                        single-line
                        hide-details
                    ></v-text-field>
                </v-col>
            </v-row>
            <v-row justify="center">
                <v-col cols="9">
                <v-data-table
                    @click:row="go_to_car_detail_page"
                    :headers="headers"
                    :items="cars"
                    :items-per-page="12"
                    class="elevation-1"
                    :search="search"
                ></v-data-table>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
 export default {
     data () {
         return {
             cars: [],
             search: '',
             headers: [
                 { text: "Car", value:"model"},
                 { text: "Customer Name", value:"customer_name"},
                 { text: "Phone Number", value:"customer_phone_number"},
             ]

         }
     },
     methods: {
         go_to_car_detail_page (car) {
             window.location.href = `/cars/${car.id}`
         },
         async get_car () {
             let url = `/api/cars/`
             let resp = await this.$axios.get(url)
             this.cars = resp.data
         }
     },
     mounted () {
         this.get_car()
     }
 }
</script>
