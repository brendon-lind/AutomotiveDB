<template>
    <div>
        <v-container>
            <v-row justify="center">
                <v-col cols="3">
                    <v-text-field
                        v-model="search"
                        append-icon="mdi-magnify"
                        label="Search"
                        width
                        dark
                        solo
                        dense
                        single-line
                        hide-details
                    ></v-text-field>
                </v-col>
                <v-col cols="3">
                    <v-dialog dark v-model="dialog" max-width="600px">
                        <template v-slot:activator="{ on }">
                            <v-btn color="primary" v-on="on">Add Customer</v-btn>
                        </template>
                        <v-card>
                            <v-card-title>
                                <span class="headline">Customer</span>
                            </v-card-title>
                            <v-card-text>
                                <v-container>
                                    <v-row>
                                        <v-col cols="12">
                                            <v-text-field v-model="customer_form.name" label="Customer Name" required></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                                <v-text-field v-model="customer_form.phone_number" label="Phone Number" required></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-text-field v-model="customer_form.description" label="Description"></v-text-field>
                                        </v-col>
                                        <v-col cols="12">
                                            <v-file-input v-model="customer_portrait" label="Profile Picture"></v-file-input>
                                        </v-col>
                                    </v-row>
                                </v-container>
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="primary" text @click="dialog = false">Close</v-btn>
                                <v-btn color="primary" text @click="add_new_customer">Save</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-dialog>
                    <v-btn color="primary">Add Vehicle</v-btn>
                </v-col>
            </v-row>
            <v-row justify="center">
                <v-col cols="9">
                    <v-data-table
                        @click:row="go_to_car_detail_page"
                        :headers="headers"
                    :items="cars"
                    :items-per-page="12"
                    dark
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
             file_form_headers: {
                 'Content-Type': 'multipart/form-data',
             },
             customer_portrait: null,
             customer_form: {
                 name: null,
                 phone_number: null,
                 description: null,
                 portrait: null,
             },
             dialog: false,
             cars: [],
             search: '',
             headers: [
                 { text: "Vehicle", value:"make_and_model"},
                 { text: "Vin", value:"vin"},
                 { text: "Customer Name", value:"customer_name"},
                 { text: "Phone Number", value:"customer_phone_number"},
             ]
         }
     },
     methods: {
         add_new_customer (){
             console.log(this.customer_form)
             let url = '/api/customers/'
             let form_data = new FormData()
             form_data.append('portrait', this.customer_portrait)

             _.forOwn(this.customer_form, function(value, key) {
                 form_data.append(key, value)
             })
             this.$axios.post(url, form_data, this.file_form_headers)
             this.dialog = false
         },
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
