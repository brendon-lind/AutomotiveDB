<template>
    <div>
        <v-container>
            <v-row justify="center">
                <v-col cols="4">
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
                <v-col class="d-flex justify-end" cols="5">
                    <v-dialog dark v-model="customer_dialog" max-width="600px">
                        <template v-slot:activator="{ on }">
                            <v-btn color="primary" v-on="on">Add Customer</v-btn>
                        </template>
                        <v-form
                            v-model="valid_customer"
                            ref="customer_form"
                        >
                            <v-card>
                                <v-card-title>
                                    <span class="headline">Customer</span>
                                </v-card-title>
                                <v-card-text>
                                        <v-container>
                                            <v-row>
                                                <v-col cols="12">
                                                    <v-text-field
                                                        v-model="customer_form.name"
                                                        label="Customer Name"
                                                        required
                                                        :rules="[required_field]"
                                                    ></v-text-field>
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
                                    <v-btn color="primary" text @click="customer_dialog = false">Close</v-btn>
                                    <v-btn color="primary" text @click="add_new_customer">Save</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-form>
                    </v-dialog>
                    <v-dialog dark v-model="vehicle_dialog" max-width="600px">
                        <template v-slot:activator="{ on }">
                            <v-btn class="ml-5" color="primary" v-on="on">Add Vehicle</v-btn>
                        </template>
                        <v-form
                            v-model="valid_vehicle"
                            ref="vehicle_form"
                        >
                            <v-card>
                                <v-card-title>
                                    <span class="headline">Vehicle</span>
                                </v-card-title>
                                <v-card-text>
                                    <v-container>
                                        <v-row>
                                            <v-col cols="12">
                                                <v-select
                                                    item-text="name"
                                                    item-value="id"
                                                    v-model="vehicle_form.customer"
                                                    :items="customers"
                                                    label="Customer"
                                                ></v-select>
                                            </v-col>
                                            <v-col cols="6">
                                                <v-text-field
                                                    v-model="vehicle_form.year"
                                                    label="Year"
                                                    required
                                                    :rules="[is_integer]"
                                                ></v-text-field>
                                            </v-col>
                                            <v-col cols="6">
                                                <v-text-field v-model="vehicle_form.make" label="Make" required></v-text-field>
                                            </v-col>
                                            <v-col cols="6">
                                                <v-text-field v-model="vehicle_form.model" label="Model"></v-text-field>
                                            </v-col>
                                            <v-col cols="6">
                                                <v-text-field v-model="vehicle_form.engine_size" label="Engine Size"></v-text-field>
                                            </v-col>
                                            <v-col cols="12">
                                                <v-text-field v-model="vehicle_form.vin" label="Vin"></v-text-field>
                                            </v-col>
                                            <v-col cols="6">
                                                <v-autocomplete
                                                    v-model="vehicle_form.engine_layout"
                                                    item-text="display_name"
                                                    item-value="value"
                                                    :items="engine_layout_options"
                                                    label="Engine Layout"
                                                ></v-autocomplete>
                                            </v-col>
                                            <v-col cols="6">
                                                <v-autocomplete
                                                    v-model="vehicle_form.fuel"
                                                    item-text="display_name"
                                                    item-value="value"
                                                    :items="fuel_options"
                                                    label="Fuel Type"
                                                ></v-autocomplete>
                                            </v-col>
                                            <v-col cols="12">
                                                <v-file-input v-model="vehicle_form.header_photo" label="Header Photo"></v-file-input>
                                            </v-col>
                                        </v-row>
                                    </v-container>
                                </v-card-text>
                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn color="primary" text @click="vehicle_dialog = false">Close</v-btn>
                                    <v-btn color="primary" text @click="add_new_vehicle">Save</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-form>
                    </v-dialog>
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
        <v-snackbar
            color="primary"
            top
            v-model="snackbar_success"
            :timeout="2000"
        >
            {{snackbar_message}}
        </v-snackbar>
    </div>
</template>

<script>
 export default {
     data () {
         return {
             customers: {},
             file_form_headers: {
                 'Content-Type': 'multipart/form-data',
             },
             customer_portrait: null,
             valid_customer: false,
             valid_vehicle: false,
             customer_form: {
                 name: '',
                 phone_number: null,
                 description: null,
                 portrait: null,
             },
             vehicle_form: {
                 customer: null,
                 year: null,
                 make: null,
                 model: null,
                 vin: null,
                 engine_size: null,
                 engine_layout: null,
                 fuel: null,
                 header_photo: null,
             },
             snackbar_message: '',
             snackbar_success: false,
             vehicle_dialog: false,
             customer_dialog: false,
             cars: [],
             engine_layout_options: [],
             fuel_options: [],
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
         required_field(value) {
             let message = 'This field is required.'
             if (!value) {
                 return message
             } else {
                 return true
             }
         },
         async add_new_customer (){
             console.log(this.customer_form)
             let url = '/api/customers/'
             let form_data = new FormData()
             form_data.append('portrait', this.customer_portrait)

             _.forOwn(this.customer_form, function(value, key) {
                 form_data.append(key, value)
             })
             try {
                 this.$refs.customer_form.validate()
                 if (!this.valid_customer) {
                     throw new Error('Invalid Customer Form')
                 }
                 await this.$axios.post(url, form_data, this.file_form_headers)
                 this.customer_dialog = false
                 this.snackbar_message = 'Customer Added'
                 this.snackbar_success = true
                 this.get_customers()
                 let that = this
                 _.forOwn(this.customer_form, function(value, key) {
                     that.customer_form[key] = null
                 })
             } catch {
                 console.log('Failed to create')
             }
         },
         async add_new_vehicle (){
             console.log(this.vehicle_form)
             let url = '/api/cars/'
             let form_data = new FormData()
             _.forOwn(this.vehicle_form, function(value, key) {
                 form_data.append(key, value)
             })
             try {
                 this.$refs.vehicle_form.validate()
                 if (!this.valid_vehicle) {
                     throw new Error('Invalid Vehicle Form')
                 }
                 await this.$axios.post(url, form_data, this.file_form_headers)
                 this.vehicle_dialog = false
                 this.snackbar_message = 'Vehicle Added'
                 this.snackbar_success = true
                 this.get_cars()
                 let that = this
                 _.forOwn(this.vehicle_form, function(value, key) {
                     that.vehicle_form[key] = null
                 })
             } catch(e) {
                 console.error(e)
                 console.log('Failed to create')
             }
         },
         go_to_car_detail_page (car) {
             window.location.href = `/cars/${car.id}`
         },
         async get_options () {
             let url ='/api/cars/'
             let resp = await this.$axios.options(url)
             this.engine_layout_options = resp.data.actions.POST.engine_layout.choices
             this.fuel_options = resp.data.actions.POST.fuel.choices
         },
         async get_cars () {
             let url = `/api/cars/`
             let resp = await this.$axios.get(url)
             this.cars = resp.data
         },
         async get_customers () {
             let url = `/api/customers/`
             let resp = await this.$axios.get(url)
             console.log(resp.data)
             this.customers = resp.data
         },
     },
     mounted () {
         this.get_cars()
         this.get_options()
         this.get_customers()
     }
 }
</script>
