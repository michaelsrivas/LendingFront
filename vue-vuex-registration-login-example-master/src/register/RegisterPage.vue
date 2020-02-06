<template>
    <div>
        <h1>Register</h1>
        <br>
        <form @submit.prevent="handleSubmit">
            <h2>Owner</h2>
            <div class="form-group">
                <label for="firstName">First Name</label>
                <input type="text" v-model="user.firstName" v-validate="'required'" name="firstName" class="form-control" :class="{ 'is-invalid': submitted && errors.has('firstName') }" />
                <div v-if="submitted && errors.has('firstName')" class="invalid-feedback">{{ errors.first('firstName') }}</div>
            </div>
            <div class="form-group">
                <label for="lastName">Last Name</label>
                <input type="text" v-model="user.lastName" v-validate="'required'" name="lastName" class="form-control" :class="{ 'is-invalid': submitted && errors.has('lastName') }" />
                <div v-if="submitted && errors.has('lastName')" class="invalid-feedback">{{ errors.first('lastName') }}</div>
            </div>
            <div class="form-group">
                <label for="ssNumber">Socual Security Number</label>
                <input type="number" v-model="user.ssNumber" v-validate="'required'" name="ssNumber" class="form-control" :class="{ 'is-invalid': submitted && errors.has('ssNumber') }" />
                <div v-if="submitted && errors.has('ssNumber')" class="invalid-feedback">{{ errors.first('ssNumber') }}</div>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" v-model="user.email" v-validate="'required'" name="email" class="form-control" :class="{ 'is-invalid': submitted && errors.has('email') }" />
                <div v-if="submitted && errors.has('email')" class="invalid-feedback">{{ errors.first('email') }}</div>
            </div>
            <div class="form-group">
                <label htmlFor="password">Password</label>
                <input type="password" v-model="user.password" v-validate="{ required: true, min: 6 }" name="password" class="form-control" :class="{ 'is-invalid': submitted && errors.has('password') }" />
                <div v-if="submitted && errors.has('password')" class="invalid-feedback">{{ errors.first('password') }}</div>
            </div>
            <div class="form-group">
                <label for="address">Address</label>
                <input type="text" v-model="user.address" v-validate="'required'" name="address" class="form-control" :class="{ 'is-invalid': submitted && errors.has('address') }" />
                <div v-if="submitted && errors.has('address')" class="invalid-feedback">{{ errors.first('address') }}</div>
            </div>
            <div class="form-group">
                <label for="city">City</label>
                <input type="text" v-model="user.city" v-validate="'required'" name="city" class="form-control" :class="{ 'is-invalid': submitted && errors.has('city') }" />
                <div v-if="submitted && errors.has('city')" class="invalid-feedback">{{ errors.first('city') }}</div>
            </div>
            <div class="form-group">
                <label for="state">State</label>
                <input type="text" v-model="user.state" v-validate="'required'" name="state" class="form-control" :class="{ 'is-invalid': submitted && errors.has('state') }" />
                <div v-if="submitted && errors.has('state')" class="invalid-feedback">{{ errors.first('state') }}</div>
            </div>
            <div class="form-group">
                <label for="postalCode">Postal Code</label>
                <input type="text" v-model="user.postalCode" v-validate="'required'" name="postalCode" class="form-control" :class="{ 'is-invalid': submitted && errors.has('postalCode') }" />
                <div v-if="submitted && errors.has('postalCode')" class="invalid-feedback">{{ errors.first('postalCode') }}</div>
            </div>

            <h2>Bussiness</h2>
            <div class="form-group">
                <label for="taxId">Tax Id</label>
                <input type="text" v-model="user.taxId" v-validate="'required'" name="taxId" class="form-control" :class="{ 'is-invalid': submitted && errors.has('taxId') }" />
                <div v-if="submitted && errors.has('taxId')" class="invalid-feedback">{{ errors.first('taxId') }}</div>
            </div>
            <div class="form-group">
                <label for="bussinessName">Bussiness Name</label>
                <input type="text" v-model="user.bussinessName" v-validate="'required'" name="bussinessName" class="form-control" :class="{ 'is-invalid': submitted && errors.has('bussinessName') }" />
                <div v-if="submitted && errors.has('bussinessName')" class="invalid-feedback">{{ errors.first('bussinessName') }}</div>
            </div>            
            <div class="form-group">
                <label for="bussinessAddress">Bussiness Address</label>
                <input type="text" v-model="user.bussinessAddress" v-validate="'required'" name="bussinessAddress" class="form-control" :class="{ 'is-invalid': submitted && errors.has('bussinessAddress') }" />
                <div v-if="submitted && errors.has('bussinessAddress')" class="invalid-feedback">{{ errors.first('bussinessAddress') }}</div>
            </div>
            <div class="form-group">
                <label for="bussinessCity">Bussiness City</label>
                <input type="text" v-model="user.bussinessCity" v-validate="'required'" name="bussinessCity" class="form-control" :class="{ 'is-invalid': submitted && errors.has('bussinessCity') }" />
                <div v-if="submitted && errors.has('bussinessCity')" class="invalid-feedback">{{ errors.first('bussinessCity') }}</div>
            </div>
            <div class="form-group">
                <label for="bussinessState">Bussiness State</label>
                <input type="text" v-model="user.bussinessState" v-validate="'required'" name="bussinessState" class="form-control" :class="{ 'is-invalid': submitted && errors.has('bussinessState') }" />
                <div v-if="submitted && errors.has('bussinessState')" class="invalid-feedback">{{ errors.first('bussinessState') }}</div>
            </div>
            <div class="form-group">
                <label for="bussinessPostalCode">Bussiness Postal Code</label>
                <input type="text" v-model="user.bussinessPostalCode" v-validate="'required'" name="bussinessPostalCode" class="form-control" :class="{ 'is-invalid': submitted && errors.has('bussinessPostalCode') }" />
                <div v-if="submitted && errors.has('bussinessPostalCode')" class="invalid-feedback">{{ errors.first('bussinessPostalCode') }}</div>
            </div>
            <div class="form-group">
                <label for="amount">Requested Amount</label>
                <input type="number" v-model="user.amount" v-validate="'required'" name="amount" class="form-control" :class="{ 'is-invalid': submitted && errors.has('amount') }" />
                <div v-if="submitted && errors.has('amount')" class="invalid-feedback">{{ errors.first('amount') }}</div>
            </div>

            <div class="form-group">
                <button class="btn btn-primary" :disabled="status.registering">Register</button>
                <img v-show="status.registering" src="data:image/gif;base64,R0lGODlhEAAQAPIAAP///wAAAMLCwkJCQgAAAGJiYoKCgpKSkiH/C05FVFNDQVBFMi4wAwEAAAAh/hpDcmVhdGVkIHdpdGggYWpheGxvYWQuaW5mbwAh+QQJCgAAACwAAAAAEAAQAAADMwi63P4wyklrE2MIOggZnAdOmGYJRbExwroUmcG2LmDEwnHQLVsYOd2mBzkYDAdKa+dIAAAh+QQJCgAAACwAAAAAEAAQAAADNAi63P5OjCEgG4QMu7DmikRxQlFUYDEZIGBMRVsaqHwctXXf7WEYB4Ag1xjihkMZsiUkKhIAIfkECQoAAAAsAAAAABAAEAAAAzYIujIjK8pByJDMlFYvBoVjHA70GU7xSUJhmKtwHPAKzLO9HMaoKwJZ7Rf8AYPDDzKpZBqfvwQAIfkECQoAAAAsAAAAABAAEAAAAzMIumIlK8oyhpHsnFZfhYumCYUhDAQxRIdhHBGqRoKw0R8DYlJd8z0fMDgsGo/IpHI5TAAAIfkECQoAAAAsAAAAABAAEAAAAzIIunInK0rnZBTwGPNMgQwmdsNgXGJUlIWEuR5oWUIpz8pAEAMe6TwfwyYsGo/IpFKSAAAh+QQJCgAAACwAAAAAEAAQAAADMwi6IMKQORfjdOe82p4wGccc4CEuQradylesojEMBgsUc2G7sDX3lQGBMLAJibufbSlKAAAh+QQJCgAAACwAAAAAEAAQAAADMgi63P7wCRHZnFVdmgHu2nFwlWCI3WGc3TSWhUFGxTAUkGCbtgENBMJAEJsxgMLWzpEAACH5BAkKAAAALAAAAAAQABAAAAMyCLrc/jDKSatlQtScKdceCAjDII7HcQ4EMTCpyrCuUBjCYRgHVtqlAiB1YhiCnlsRkAAAOwAAAAAAAAAAAA==" />
                <router-link to="/login" class="btn btn-link">Cancel</router-link>
            </div>
        </form>
    </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
    data () {
        return {
            user: {
                firstName: '',
                lastName: '',
                ssNumber: '',
                email: '',
                password: '',
                address: '',
                city: '',
                state: '',
                postalCode: '',
                taxId: '',
                bussinessName:'',
                bussinessAddress: '',
                bussinessCity: '',
                bussinessState: '',
                bussinessPostalCode: '',
                amount: '',
                deal: ''
            },
            submitted: false
        }
    },
    computed: {
        ...mapState('account', ['status'])
    },
    methods: {
        ...mapActions('account', ['register']),
        handleSubmit(e) {
            this.submitted = true;
            if (parseInt(this.user.amount, 10) > 50000){
                this.user.deal = 'Declined'
            }
            else if(parseInt(this.user.amount, 10) === 50000){
                this.user.deal = 'Undecided'
            }
            else{
                this.user.deal = 'Approved'
            }
            this.$validator.validate().then(valid => {
                if (valid) {
                    this.register(this.user);
                }
            });
        }
    }
};
</script>