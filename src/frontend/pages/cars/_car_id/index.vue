<template>
    <div>
        <v-container >
            <v-row
                justify="center"
            >
                <v-col
                    cols="11"
                >
                    <v-card
                        class="car-header"
                        dark
                        fluid
                    >
                        <v-container>
                            <v-row
                                justify="space-between"
                            >
                                <v-col
                                    cols="3"
                                >
                                    <v-img
                                        :src="car.customer_portrait"
                                        width="150px"
                                        height="150px"
                                        contain
                                    ></v-img>
                                    <v-spacer></v-spacer>
                                    <h4>
                                        {{car.customer_name}}
                                    </h4>
                                    <h4>
                                        {{car.customer_phone_number}}
                                    </h4>
                                    <h4>
                                        {{car.customer_description}}
                                    </h4>
                                </v-col>
                                <v-col>
                                    <h4>
                                        {{car.make_and_model}}
                                    </h4>
                                    <h4>
                                        Year: {{car.year}}
                                    </h4>
                                    <h4>
                                        VIN: {{car.vin}}
                                    </h4>
                                    <h4>
                                        {{car.engine_size}} Liter
                                        {{car.engine_layout}}
                                    </h4>
                                    <h4>
                                        Fuel Type: {{car.fuel}}
                                    </h4>
                                    <v-btn class="ml-5" color="primary" @click="edit_vehicle">Edit Vehicle</v-btn>
                                    <v-dialog dark v-model="edit_vehicle_dialog" max-width="600px">
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
                                                                v-model="edit_vehicle_form.customer"
                                                                :items="customers"
                                                                label="Customer"
                                                            ></v-select>
                                                        </v-col>
                                                        <v-col cols="6">
                                                            <v-text-field v-model="edit_vehicle_form.year" label="Year" required></v-text-field>
                                                        </v-col>
                                                        <v-col cols="6">
                                                            <v-text-field v-model="edit_vehicle_form.make" label="Make" required></v-text-field>
                                                        </v-col>
                                                        <v-col cols="6">
                                                            <v-text-field v-model="edit_vehicle_form.model" label="Model"></v-text-field>
                                                        </v-col>
                                                        <v-col cols="6">
                                                            <v-text-field v-model="edit_vehicle_form.engine_size" label="Engine Size"></v-text-field>
                                                        </v-col>
                                                        <v-col cols="12">
                                                            <v-text-field v-model="edit_vehicle_form.vin" label="Vin"></v-text-field>
                                                        </v-col>
                                                        <v-col cols="6">
                                                            <v-autocomplete
                                                                v-model="edit_vehicle_form.engine_layout"
                                                                item-text="display_name"
                                                                item-value="value"
                                                                :items="engine_layout_options"
                                                                label="Engine Layout"
                                                            ></v-autocomplete>
                                                        </v-col>
                                                        <v-col cols="6">
                                                            <v-autocomplete
                                                                v-model="edit_vehicle_form.fuel"
                                                                item-text="display_name"
                                                                item-value="value"
                                                                :items="fuel_options"
                                                                label="Fuel Type"
                                                            ></v-autocomplete>
                                                        </v-col>
                                                        <v-col cols="12">
                                                            <v-file-input v-model="edit_vehicle_form.header_photo" label="Header Photo"></v-file-input>
                                                        </v-col>
                                                    </v-row>
                                                </v-container>
                                            </v-card-text>
                                            <v-card-actions>
                                                <v-spacer></v-spacer>
                                                <v-btn color="primary" text @click="edit_vehicle_dialog = false">Close</v-btn>
                                                <v-btn color="primary" text @click.stop="save_vehicle">Save</v-btn>
                                            </v-card-actions>
                                        </v-card>
                                    </v-dialog>
                                </v-col>
                                <v-col>
                                    <v-img
                                        :src="car.header_photo"
                                        width="400px"
                                        height="200px"
                                        contain
                                    ></v-img>
                                </v-col>
                                <v-col
                                    cols="3"
                                    align="end"
                                >
                                    <v-btn
                                        @click="test"
                                    >
                                        Test
                                    </v-btn>
                                    <v-menu>
                                        <template v-slot:activator="{ on }">
                                            <v-btn
                                                v-on="on"
                                                class="mb-4 grey darken-2"
                                            >
                                                General Files
                                            </v-btn>
                                        </template>

                                        <v-list>
                                            <v-list-item
                                                @click="new_general = true"
                                            >
                                                <v-list-item-title>
                                                    <v-icon>mdi-plus</v-icon>
                                                    Add General File
                                                </v-list-item-title>


                                            </v-list-item>
                                            <v-list-item
                                                v-for="(item, index) in general_files"
                                                :key="index"
                                                link
                                                :href="item.file"
                                            >
                                                <v-list-item-title>{{ item.name }}</v-list-item-title>
                                            </v-list-item>
                                        </v-list>
                                    </v-menu>
                                    <v-menu>
                                        <template v-slot:activator="{ on }">
                                            <v-btn
                                                v-on="on"
                                                class="mb-4 grey darken-2"
                                            >
                                                Invoice Files
                                            </v-btn>
                                        </template>

                                        <v-list>
                                            <v-list-item
                                                @click="new_invoice = true"
                                            >
                                                <v-list-item-title>
                                                    <v-icon>mdi-plus</v-icon>
                                                    Add Invoice File
                                                </v-list-item-title>


                                            </v-list-item>
                                            <v-list-item
                                                v-for="(item, index) in invoice_files"
                                                :key="index"
                                                link
                                                :href="item.file"
                                            >
                                                <v-list-item-title>{{ item.name }}</v-list-item-title>
                                            </v-list-item>
                                        </v-list>
                                    </v-menu>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card>
                </v-col>
            </v-row>

            <v-row
                justify="center"
            >
                <v-col
                    cols="11"
                >
                    <v-card
                        class="car-comments"
                        fluid
                        dark
                        justify="end"
                    >
                        <v-container>
                            <v-row>
                                <v-col
                                    class="d-flex justify-end comments-header"
                                >
                                    <v-btn
                                        v-if="!new_comment"
                                        @click="create_new_comment"
                                        color="primary"
                                    >
                                        <v-icon>mdi-plus</v-icon>
                                        Add Comment
                                    </v-btn>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <v-textarea
                                        fluid
                                        v-if="new_comment"
                                        v-model="new_comment_data"
                                    />
                                    <v-btn
                                        v-if="new_comment"
                                        color="primary"
                                        @click="save_comment"
                                    >
                                        <v-icon>mdi-plus</v-icon>
                                        Save New Comment
                                    </v-btn>
                                    <v-btn
                                        v-if="new_comment"
                                        color="primary"
                                        @click="new_comment=false"
                                    >
                                        Cancel
                                    </v-btn>
                                    <v-list>
                                        <v-list-item
                                            v-for="comment in comments"
                                            class="comment"
                                        >
                                            <v-container>
                                                <v-row
                                                    fluid
                                                >
                                                    <v-list-item-content
                                                        class="headline"
                                                    >
                                                        <v-list-item-subtitle
                                                            class="headline grey--text"
                                                        >
                                                            {{format_date(comment.date_created)}}
                                                        </v-list-item-subtitle>
                                                        {{comment.content}}
                                                    </v-list-item-content>
                                                    <v-btn
                                                        @click="edit_comment(comment)"
                                                    >
                                                        Edit
                                                        <v-icon>
                                                            mdi-pencil
                                                        </v-icon>
                                                    </v-btn>
                                                    <v-btn
                                                        @click="delete_comment(comment)"
                                                    >
                                                        Delete
                                                        <v-icon>
                                                            mdi-delete
                                                        </v-icon>
                                                    </v-btn>
                                                </v-row>
                                                <v-row
                                                    fluid
                                                >
                                                    <v-col>
                                                        <v-textarea
                                                                fluid
                                                            v-if="edit_comment_id===comment.id"
                                                            v-model="edit_comment_data"
                                                        />
                                                        <v-btn
                                                            v-if="edit_comment_id===comment.id"
                                                            color="primary"
                                                            @click="save_comment"
                                                        >
                                                            Save Comment
                                                        </v-btn>
                                                        <v-btn
                                                            v-if="edit_comment_id===comment.id"
                                                            color="primary"
                                                            @click="edit_comment_id=null"
                                                        >
                                                            Cancel
                                                        </v-btn>
                                                    </v-col>
                                                </v-row>
                                            </v-container>
                                        </v-list-item>
                                    </v-list>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card>
                </v-col>
            </v-row>

        </v-container>
        <v-dialog v-model="new_general" max-width="600px">
            <v-card>
                <v-card-title>
                    <span class="headline">New General File</span>
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-col cols="12" sm="6">
                                <v-file-input v-model="new_general_file" label="General File"/>
                            </v-col>
                        </v-row>
                    </v-container>
                    <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="new_general = false">Close</v-btn>
                    <v-btn color="blue darken-1" text @click="save_files">Save</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <v-dialog v-model="new_invoice" max-width="600px">
            <v-card>
                <v-card-title>
                    <span class="headline">New Invoice File</span>
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <v-row>
                            <v-col cols="12" sm="6">
                                <v-file-input v-model="new_invoice_file" label="Invoice File"/>
                            </v-col>
                        </v-row>
                    </v-container>
                    <small>*indicates required field</small>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="blue darken-1" text @click="new_invoice = false">Close</v-btn>
                    <v-btn color="blue darken-1" text @click="save_files">Save</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                file_form_headers: {
                    'Content-Type': 'multipart/form-data',
                },
                car: {},
                comments: [],
                new_comment_data: '',
                new_comment: false,
                edit_comment_id: null,
                edit_comment_data: '',
                new_invoice: null,
                new_general: null,
                new_invoice_file: null,
                new_general_file: null,
                edit_vehicle_dialog: false,
                edit_vehicle_form: {
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
                engine_layout_options: [],
                fuel_options: [],
                customers: [],
            }
        },
        methods: {
            test() {

                console.log(this.car)
                _.forOwn(this.edit_vehicle_form, (value, key) => {
                    this.edit_vehicle_form[key] = this.car[key]
                })
                console.log(this.edit_vehicle_form)
            },
            edit_vehicle() {
                _.forOwn(this.edit_vehicle_form, (value, key) => {
                    if (key === 'header_photo') {
                        return
                    }
                    this.edit_vehicle_form[key] = this.car[key]
                    console.log(key)
                })
                this.edit_vehicle_dialog = true
            },
            async get_car() {
                try {
                    let resp = await this.$axios.get(`/api/cars/${this.$route.params.car_id}`)
                    this.car = resp.data
                } catch (e) {
                    console.log(e)
                    console.log("Failed to get car.")
                }
            },
            async get_comments() {
                try {
                    let resp = await this.$axios.get(`/api/comments/?car=${this.$route.params.car_id}`)
                    this.comments = resp.data
                } catch (e) {
                    console.log(e)
                    console.log("Failed to get comments.")
                }
            },
            create_new_comment() {
                this.new_comment_data = ''
                this.new_comment = true
            },
            async edit_comment(comment) {
                this.edit_comment_id = comment.id
                this.edit_comment_data = comment.content
            },
            async delete_comment(comment) {
                if(confirm("Are you sure you want to delete this comment?")) {
                    try {
                        let resp = await this.$axios.delete(`/api/comments/${comment.id}/`)
                        this.get_comments()
                    } catch (e) {
                        console.log(e)
                        console.log("Failed to delete comment.")
                    }
                }
            },
            async save_comment() {
                try {
                    if (this.edit_comment_id) {
                        let resp = await this.$axios.patch(`/api/comments/${this.edit_comment_id}/`, {
                                content: this.edit_comment_data
                            }
                        )
                        this.edit_comment_id = null
                        this.get_comments()
                    }
                    else if (this.new_comment) {
                        if (this.new_comment_data.length > 0) {
                            let resp = await this.$axios.post(`/api/comments/`, {
                                car: this.$route.params.car_id,
                                content: this.new_comment_data
                            })
                            this.new_comment = false
                            this.get_comments()
                        }
                    }
                } catch (e) {
                    console.log(e)
                    console.log("Failed to create comment.")
                }
            },
            async save_files() {
                try {
                    if (this.new_general_file) {
                        let form_data = new FormData()
                        form_data.append('car', this.$route.params.car_id)
                        form_data.append('type', 'GENERAL')
                        form_data.append('file', this.new_general_file)
                        let resp = await this.$axios.post(
                            `/api/car_files/`,
                            form_data,
                            {
                                'Content-Type': 'multipart/form-data'
                            }
                        )
                    }
                    if (this.new_invoice_file) {
                        let form_data = new FormData()
                        form_data.append('car', this.$route.params.car_id)
                        form_data.append('type', 'INVOICE')
                        form_data.append('file', this.new_invoice_file)
                        let resp = await this.$axios.post(
                            `/api/car_files/`,
                            form_data,
                            {
                                'Content-Type': 'multipart/form-data'
                            }
                        )
                    }
                    this.new_invoice = false
                    this.new_general = false
                    this.new_invoice_file = null
                    this.new_general_file = null
                    this.get_car()
                } catch (e) {
                    console.log(e)
                    console.log("Failed to upload files.")
                }
            },
            async save_vehicle() {
                let url = `/api/cars/${this.$route.params.car_id}/`
                let form_data = new FormData()
                let that = this
                console.log('save_vehicle')

                _.forOwn(this.edit_vehicle_form, function(value, key) {
                    if (key === 'header_photo') {
                        if (!that.edit_vehicle_form.header_photo) {
                            return
                        }
                    }
                    form_data.append(key, value)
                })
                try {
                    await this.$axios.patch(url, form_data, this.file_form_headers)
                    this.vehicle_dialog = false
                    this.snackbar_message = 'Vehicle Edited'
                    this.snackbar_success = true
                    this.get_car()
                } catch(e) {
                    console.error(e)
                    console.log('Failed to create')
                }
            },
            format_date(datestring) {
                return this.$moment(datestring).format("dddd, MMMM Do YYYY, h:mm:ss a")
            },
            async get_customers () {
                let url = `/api/customers/`
                let resp = await this.$axios.get(url)
                this.customers = resp.data
            },
            async get_options () {
                let url ='/api/cars/'
                let resp = await this.$axios.options(url)
                this.engine_layout_options = resp.data.actions.POST.engine_layout.choices
                this.fuel_options = resp.data.actions.POST.fuel.choices
            },
        },
        computed: {
            general_files() {
                if (this.car.files) {
                    return this.car.files.filter(f => f.type == 'GENERAL')
                } else {
                    return []
                }
            },
            invoice_files() {
                if (this.car.files) {
                    return this.car.files.filter(f => f.type == 'INVOICE')
                } else {
                    return []
                }
            },
        },
        async mounted() {
            this.get_customers()
            this.get_car()
            this.get_comments()
        }
    }
</script>

<style scoped>
    .car-header {
        padding: 45px;
    }

    .car-comments {
        padding: 45px;
    }

    .comments-header {
        padding-right: 20px;
    }

    .comment {
        margin: 45px;
    }
</style>
