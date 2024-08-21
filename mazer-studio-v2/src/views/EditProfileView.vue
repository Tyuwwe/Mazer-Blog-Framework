<script setup>
import CopyRight from '../components/CopyRight.vue'
</script>

<template>
    <div class="editProfileContainer">
        <div class="row editCols">
            <div class="col-3 cols-left">
                <div class="list-group" id="list-tab" role="tablist">
                    <a class="list-group-item list-group-item-action active" id="list-home-list" data-bs-toggle="list" href="#list-home" role="tab" aria-controls="list-home">{{ $t('edit.home') }}</a>
                    <a class="list-group-item list-group-item-action" id="list-profile-list" data-bs-toggle="list" href="#list-profile" role="tab" aria-controls="list-profile">{{ $t('edit.profile') }}</a>
                    <a class="list-group-item list-group-item-action" id="list-messages-list" data-bs-toggle="list" href="#list-messages" role="tab" aria-controls="list-messages">{{ $t('edit.message') }}</a>
                    <a class="list-group-item list-group-item-action" id="list-settings-list" data-bs-toggle="list" href="#list-settings" role="tab" aria-controls="list-settings">{{ $t('edit.account') }}</a>
                    <a class="list-group-item list-group-item-action" id="list-privacy-list" data-bs-toggle="list" href="#list-privacy" role="tab" aria-controls="list-privacy">{{ $t('edit.privacy') }}</a>
                </div>
            </div>
            <div class="col-8 cols-right">
                <div class="tab-content" id="nav-tabContent">
                    <div class="tab-pane fade show active" id="list-home" role="tabpanel" aria-labelledby="list-home-list">
                        <h2 class="mb-3">{{ $t('edit.home_title') }}</h2>
                        <div class="wip">{{ $t('common.wip') }}</div>
                    </div>
                    <div class="tab-pane fade" id="list-profile" role="tabpanel" aria-labelledby="list-profile-list">
                        <h2 class="mb-3">{{ $t('edit.profile_title') }}</h2>
                        <div class="avtContainer mb-3">
                            <img :src="serverUrl + userForm.avt" alt="Avatar" class="avt-img">
                        </div>
                        <label for="avatarIptVis" class="form-label">{{ $t('edit.avt') }}</label>
                        <div class="input-group mb-3">
                            <button @click="uploadAvatar()" class="btn btn-outline-secondary" type="button" id="Avatar-Btn">
                                {{ $t('editor.modal_form_upload') }}</button>
                            <input id="avatarIptVis" type="text" class="form-control" :placeholder="userForm.avt"
                            aria-label="Avatar" aria-describedby="Avatar-Btn" disabled>
                        </div>
                        <div class="mb-3">
                            <label for="exampleFormControlTextarea1" class="form-label">{{ $t('edit.desc') }}</label>
                            <textarea v-model="userForm.desc" class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
                        </div>
                        <button @click="updateUserData()" type="button" class="btn btn-outline-primary" style="width: 100%;">{{ $t('edit.submit') }}</button>
                    </div>
                    <div class="tab-pane fade" id="list-messages" role="tabpanel" aria-labelledby="list-messages-list">
                        <h2 class="mb-3">{{ $t('edit.message_title') }}</h2>
                        <div class="wip">{{ $t('common.wip') }}</div>
                    </div>
                    <div class="tab-pane fade" id="list-settings" role="tabpanel" aria-labelledby="list-settings-list">
                        <h2 class="mb-3">{{ $t('edit.account_title') }}</h2>
                        <div class="mb-3">
                            <label for="UsernameIpt" class="form-label">{{ $t('edit.username') }}</label>
                            <div class="input-group">
                                <input type="password" hidden>
                                <input v-model="userForm.username" id="UsernameIpt" type="text" class="form-control rounded-start" :placeholder="$t('edit.usr_ph')" aria-label="New Username" autocomplete="new-password">
                                <button class="btn btn-outline-secondary" type="button" id="button-addon2">{{ $t('edit.apply') }}</button>
                            </div>
                            <div class="form-text">{{ $t('edit.username_text') }} <span style="font-weight: bold;">{{ origin }}/user/{{ userForm.username.replaceAll(' ', '_') }}</span></div>
                        </div>
                        <div class="mb-3">
                            <label for="PasswdIpt" class="form-label">{{ $t('edit.password') }}</label>
                            <div class="input-group mb-1">
                                <input type="password" hidden>
                                <input @input="pswOnChange()" v-model="userForm.password" id="PasswdIpt" type="password" class="form-control rounded-start" :placeholder="$t('edit.psw_ph')" aria-label="New Password" autocomplete="new-password">
                                <button class="btn btn-outline-secondary" type="button" id="button-addon2">{{ $t('edit.apply') }}</button>
                            </div>
                            <div style="height: 5px" class="progress mb-1" role="progressbar" aria-label="Example with label" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">
                                <div id="pswProgress" class="progress-bar" style="width: 0%"></div>
                            </div>
                            <div class="form-text">{{ $t('edit.password_text') }}<span style="color: var(--bs-danger);" id="sLvl">{{ secureLvl }}</span></div>
                        </div>
                        <button type="button" class="btn btn-outline-danger" style="width: 100%;" data-bs-toggle="modal" data-bs-target="#deleteConfirmModal">{{ $t('edit.delete_acc') }}</button>
                    </div>
                    <div class="tab-pane fade" id="list-privacy" role="tabpanel" aria-labelledby="list-privacy-list">
                        <h2 class="mb-3">{{ $t('edit.privacy_title') }}</h2>
                        <div class="wip">{{ $t('common.wip') }}</div>
                    </div>
                </div>
            </div>
        </div>
        <CopyRight class="mt-5" />
    </div>

    <div class="modal fade" id="deleteConfirmModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5 text-reset">{{ $t('edit.warning') }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="warning-text mb-1">{{ $t('edit.warning_text') }}</div>
          <div class="warning-text mb-3">{{ $t('edit.warning_text_tPassword') }}</div>
          <div class="form-floating mb-3">
            <input v-model="userForm.password" type="password" class="form-control" id="floatingConfirmPassword" placeholder="">
            <label for="floatingConfirmPassword">{{ $t('topbar.password') }}</label>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-danger" @click="handleDel()">{{ $t('edit.delete') }}</button>
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ $t('topbar.close') }}</button>
        </div>
      </div>
    </div>
  </div>

  <input @change="handleUploadAvt()" accept="image/*" ref="avtFile" id="avtFileIptHid" style="display: none;" type="file">
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            jwt: localStorage.getItem('jwt'),
            origin: location.origin,
            userForm: {
                username: '',
                password: '',
                desc: '',
                email: '',
                avt: ''
            },
            secureLvl: this.$t('edit.lvl_low'),
            serverUrl: this.$server
        }
    },
    methods: {
        async updateUserData() {
            let putData = {
                username: this.userForm.username,
                avt: this.userForm.avt,
                desc: this.userForm.desc
            }
            const res = axios.put(this.$server + "/api/user", putData, {
                headers: {
                'Authorization': 'Bearer ' + localStorage.getItem('jwt')
                }
            })
        },
        async handleUploadAvt() {
            if (this.$refs.avtFile.files[0]) {
                const avtFile = this.$refs.avtFile.files[0]
                const formData = new FormData();
                formData.append('file', avtFile);
                const res = axios.post(this.$server + "/api/uploadImage", formData, {
                    headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('jwt')
                    }
                })
                console.log(res)
                res.then((value) => {
                    this.userForm.avt = value.data.url;
                })
            }
            else {

            }
        },
        uploadAvatar() {
            document.getElementById('avtFileIptHid').click()
        },
        async fetchUserData() {
            const response = await axios.get(this.$server + '/api/users', {
                headers: {
                    'Authorization': 'Bearer ' + this.jwt,
                },
            });
            this.userForm.username = response.data.usr;
            this.userForm.desc = response.data.usr_desc;
            this.userForm.email = response.data.email;
            this.userForm.avt = response.data.avt;
            // console.log(response.data)
        },
        async handleDel() {

        },
        getLvl(val) {
            var level = 0;
            if (val.length < 6) return 0;
            if (/\d/.test(val)) level++; //数字
            if (/[a-z]/.test(val)) level++; //小写
            if (/[A-Z]/.test(val)) level++; //大写
            if (/\W/.test(val)) level++; //特殊字符

            return level;
        },
        pswOnChange() {
            let lvl = this.getLvl(this.userForm.password);
            let prges = document.getElementById('pswProgress');
            let sLvl = document.getElementById('sLvl');
            prges.style.width = (100/4) * lvl + '%'
            // console.log(lvl)
            if (lvl < 1) {
                this.secureLvl = this.$t('edit.lvl_low')
                prges.setAttribute('class', 'progress-bar bg-danger')
                sLvl.style.color = 'var(--bs-danger)'
            }
            else if (lvl == 2) {
                this.secureLvl = this.$t('edit.lvl_med')
                prges.setAttribute('class', 'progress-bar bg-warning')
                sLvl.style.color = 'var(--bs-warning)'
            }
            else if (lvl == 3) {
                this.secureLvl = this.$t('edit.lvl_high')
                prges.setAttribute('class', 'progress-bar bg-success')
                sLvl.style.color = 'var(--bs-success)'
            }
            else if (lvl == 4) {
                this.secureLvl = this.$t('edit.lvl_vhigh')
                prges.setAttribute('class', 'progress-bar bg-success')
                sLvl.style.color = 'var(--bs-success)'
            }
        }
    },
    mounted() {
        this.fetchUserData()
    }
}
</script>

<style scoped>
.editProfileContainer {
    max-width: 1200px;
    min-width: 350px;
    width: 75%;
    margin: auto;
    margin-top: 100px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.editCols {
    width: 100%;

}

.warning-text {
    color: var(--bs-danger);
    font-weight: bold;
}

.avtContainer {
    width: 200px;
    height: 200px;
    overflow: hidden;
    border-radius: 5px;
}

.avt-img {
    height: 100%;
    object-fit: cover;
}

.avt-img:hover {
    filter: brightness(0.9);
}

@media only screen and (max-width: 750px) {
    .editCols {
        flex-direction: column;
    }

    .cols-left, .cols-right {
        width: 100%;
    }

    .cols-left {
        margin-bottom: 12px;
    }
}
</style>