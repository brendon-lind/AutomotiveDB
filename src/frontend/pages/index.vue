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
             customers: [
                 { name: 'John', phone_number: '(123)456-7890'},
                 { name: 'Sue', phone_number: '(123)456-7890'},
                 { name: 'Mary', phone_number: '(123)456-7890'},
                 { name: 'Jesus', phone_number: '(123)456-7890'},
                 { name: 'Allah', phone_number: '(123)456-7890'},
                 { name: 'Marduk', phone_number: '(123)456-7890'},
                 { name: 'John', phone_number: '(123)456-7890'},
                 { name: 'Sue', phone_number: '(123)456-7890'},
                 { name: 'Mary', phone_number: '(123)456-7890'},
                 { name: 'Jesus', phone_number: '(123)456-7890'},
                 { name: 'Allah', phone_number: '(123)456-7890'},
                 { name: 'Marduk', phone_number: '(123)456-7890'},
                 { name: 'John', phone_number: '(123)456-7890'},
                 { name: 'Sue', phone_number: '(123)456-7890'},
                 { name: 'Mary', phone_number: '(123)456-7890'},
                 { name: 'Jesus', phone_number: '(123)456-7890'},
                 { name: 'Allah', phone_number: '(123)456-7890'},
                 { name: 'Marduk', phone_number: '(123)456-7890'},
             ],
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
     }
 }
</script>
