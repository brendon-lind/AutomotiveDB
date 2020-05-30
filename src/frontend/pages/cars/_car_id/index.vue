<template>
    <div>
        <v-card
            fluid
        >
            {{car.model}}
            {{car.customer_name}}
            {{car.customer_phone_number}}
        </v-card>
        <v-card
            fluid
        >
            <v-btn
                v-if="!new_comment"
                @click="new_comment = true"
            >
                <v-icon>mdi-plus</v-icon>
                Add Comment
            </v-btn>
            <v-textarea
                v-if="new_comment"
                v-model="new_comment_data"
            />
            <v-btn
                v-if="new_comment"
                class="green white--text"
                @click="save_comment"
            >
                <v-icon>mdi-plus</v-icon>
                Save New Comment
            </v-btn>
            <v-list>
                <v-list-item
                    v-for="comment in comments"
                >
                    {{comment.date_created}}
                    {{comment.content}}
                </v-list-item>
            </v-list>
        </v-card>
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
        },
        async mounted() {
            this.get_car()
            this.get_comments()
        }
    }
</script>

<style scoped>

</style>
