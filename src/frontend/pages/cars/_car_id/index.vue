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
                                    <h4
                                        class="display-3"
                                    >
                                        {{car.model}}
                                    </h4>
                                    <h4>
                                        {{car.customer_name}}
                                    </h4>
                                    <h4>
                                        {{car.customer_phone_number}}
                                    </h4>
                                    <h4>
                                        VIN: {{car.vin}}
                                    </h4>
                                </v-col>
                                <v-col
                                    cols="3"
                                    align="end"
                                >
                                    <v-btn
                                        class="mb-4 grey darken-2"
                                    >
                                        General Files
                                    </v-btn>
                                    <v-btn
                                        class="grey darken-2"
                                    >
                                        Invoice Files
                                    </v-btn>
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
                                        @click="add_comment"
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

                                        </v-list-item>
                                    </v-list>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card>
                </v-col>
            </v-row>

        </v-container>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                car: {},
                comments: [],
                new_comment_data: '',
                new_comment: false,
            }
        },
        methods: {
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
            async save_comment() {
                try {
                    if (this.new_comment_data.length > 0) {
                        let resp = await this.$axios.post(`/api/comments/`, {
                            car: this.$route.params.car_id,
                            content: this.new_comment_data
                        })
                        this.new_comment = false
                        this.get_comments()
                    }
                } catch (e) {
                    console.log(e)
                    console.log("Failed to create comment.")
                }
            },
            format_date(datestring) {
                return this.$moment(datestring).format("dddd, MMMM Do YYYY, h:mm:ss a")
            },
            add_comment() {
                this.new_comment_data = ''
                this.new_comment = true
                console.log('cleared new_comment_data')
                console.log(self.new_comment_data)
            }
        },
        async mounted() {
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
