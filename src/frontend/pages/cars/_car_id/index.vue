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
                    @click:row="go_to_customer_detail_page"
                    :headers="headers"
                    :items="customers"
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
             customers: [],
             search: '',
             headers: [
                 { text: "Customer Name", value:"name",
                     align: 'start',
                     sortable: false,
                     value: 'name',
                 },
                 { text: "Phone Number", value:"phone_number"},
             ]

         }
     },
     methods: {
         go_to_customer_detail_page (customer) {
             window.location.href = `/${customer.id}`
         },
         async get_customers () {
             let url = `/api/customers/`
             let resp = await this.$axios.get(url)
             this.customers = resp.data
         }
     },
     mounted () {
         this.get_customers()
     }
 }
</script>
