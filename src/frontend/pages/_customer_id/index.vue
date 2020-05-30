<template>
    <v-container>
        <v-row>
            <v-col cols="3">
                <v-card
                    :height="400"
                >
<!--                    class="mx-auto"-->
<!--                    max-width="344"-->
<!--                    outlined-->

                    <v-container>
                        <v-list-item three-line>
                            <v-list-item-content>
                                <v-list class="notes-header">{{ customer.name}}</v-list>
                                <v-list-item-subtitle>{{ customer.description }}</v-list-item-subtitle>
                            </v-list-item-content>

                           <v-avatar
                               size="150px"
                        >
                               <img
                                   alt="Avatar"
                                   :src="customer.portrait"
                               >
                           </v-avatar>



                        </v-list-item>
                    </v-container>
                    <v-card-actions>
                        <v-btn text>Button</v-btn>
                        <v-btn text>Button</v-btn>
                    </v-card-actions>
                </v-card>
            </v-col>
            <v-col>
                <v-card
                    :height="400"
                >
                    <p class="notes-header text-center">Invoices</p>
                </v-card>
            </v-col>
            <v-col cols="6">
                <v-card>
                    <v-container>
                        <p class="notes-header text-center">Notes</p>
                        <p class="text-justify">
                            Mauris sagittis in erat vel pharetra. Pellentesque sed sagittis felis, id cursus diam. Donec vitae posuere neque. Sed feugiat eget felis at vulputate. Aliquam libero magna, fermentum gravida lobortis sit amet, tristique sed leo. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Praesent finibus viverra magna ac volutpat. Aenean efficitur consequat elit. Nullam condimentum quis nunc et aliquet. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
                        </p>
                    </v-container>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
    export default {
        data () {
            return {
                 customer: {}
            }
        },
        methods: {
            async get_customer () {
                let url = `/api/customers/${this.$route.params.customer_id}`
                let resp = await this.$axios.get(url)
                this.customer = resp.data
            }

        },
        mounted () {
            this.get_customer()
        }
    }


</script>
<style scoped>
    .notes-header {
        font-size: 2.5em;
    }
</style>
