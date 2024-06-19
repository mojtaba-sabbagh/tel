<script>
  import DropDown from './elements/DropDown.vue';
  import InputText from './elements/InputText.vue';
  import TableResults from './TableResults.vue';
  import { serverUrl } from '../../settings';
  import axios from 'axios';

   export default {
        data() {
          return {
            family: '',
            searchStart: false,
            mainDepOptions: Object,
            mainSubDepOptions: Object,
            subSubDepOptions: Object,
            errorMessage: '',
            searchResults: null,
            finalDep: '',
            mainDep: '',
            subDep: '',
            subSubDep: '',
            next: null,
            pre: null,
            len: 0,
            offset: 0,
            pageSize: 50,
            searchBy: 'sname',
            finalPost: 0,
          }
        },
        components: {
          DropDown,
          InputText,
          TableResults,
        },
        methods:{
          depList0(){
             axios({
                    method: 'get',
                    url: serverUrl+'/tel/deps/?level=0',
                    headers: {"Content-Type": "application/json"},
                    })
                .then(response => {
                    this.mainDepOptions = response.data;
                })
                .catch(error => {
                        this.errorMessage = error //'خطایی در گرفتن اطلاعات کاربر رخ داد'; //error.data
                });
          },
          depList1(sdep){
             axios({
                    method: 'get',
                    url: serverUrl+'/tel/deps/?level=1'+'&super-dep='+sdep,
                    headers: {"Content-Type": "application/json"},
                    })
                .then(response => {
                    this.mainSubDepOptions = response.data;
                })
                .catch(error => {
                        this.errorMessage = error //'خطایی در گرفتن اطلاعات کاربر رخ داد'; //error.data
                });
          },
          depList2(sdep){
             axios({
                    method: 'get',
                    url: serverUrl+'/tel/deps/?level=2'+'&super-dep='+sdep,
                    headers: {"Content-Type": "application/json"},
                    })
                .then(response => {
                    this.subSubDepOptions = response.data;
                })
                .catch(error => {
                        this.errorMessage = error //'خطایی در گرفتن اطلاعات کاربر رخ داد'; //error.data
                });
          },
          postList(){
            axios({
                    method: 'get',
                    url: serverUrl+'/tel/posts/',
                    headers: {"Content-Type": "application/json"},
                    })
                .then(response => {
                    this.searchPostOptions = response.data;
                })
                .catch(error => {
                        this.errorMessage = error //'خطایی در گرفتن اطلاعات کاربر رخ داد'; //error.data
                });
          },
          updateFamily(newValue) {
            this.family = newValue;
            return
          },
          updateErrorArray(){
          },
          updateDep(newValue){
            if (newValue && newValue != '0'){
              this.mainDep = newValue;
              this.finalDep = newValue;
              this.mainSubDepOptions = this.depList1(this.finalDep);
            }
            else {
              this.mainDep = '';
              this.finalDep = '';
            }
          },
          updateSubDep(newValue){
            if (newValue && newValue != '0'){
              this.subDep = newValue;
              this.finalDep = newValue;
              this.subSubDepOptions = this.depList2(this.finalDep);
            } 
            else {
              this.subDep = '';
              this.updateDep(this.mainDep);
            }
          },
          updateSubSubDep(newValue){
            if (newValue && newValue != '0'){
              this.subSubDep = newValue;
              this.finalDep = newValue;
            }
            else {
              this.subSubDep = '';
              this.updateSubDep(this.subDep);
            }
          },
          updateSearchPost(newValue){
             if (newValue && newValue != '0'){
              this.finalPost = newValue;
            }
            else {
              this.finalPost = 0;
            }
          },
          submitSearch(){
            let q = '';
            let dep = this.finalDep;
            this.searchStart = true;
            let url = '';
            this.offset = 0;
            if (this.sname){
              q = this.family;
              url = serverUrl+'/tel/byname/';
            }
            else if (this.spost) {
              q = this.finalPost;
              url = serverUrl+'/tel/bypost/';
            }
            else {
              return;
            }
            if (q && dep){
              //url = url + '?q=' + q + '&dep=' + dep;
              url = url + dep + "/" + q + "/";
            } else if (q && !dep){
              //url = url + '?q=' + q;
              url = url + "0" + "/" + q + "/";
            } else if (!q && dep) {
              //url = url + '?dep=' + dep;
              url = url + dep + "/" + "0" + "/";
            }
            else {
              url = url + "0/0/";
            }
          //search api call
          this.getPage(url);
          },
          updatefamily(newValue) {
            this.family = newValue
          },
          submitSearchEnter(){
            $event.target.blur();
            this.submitSearch();
          },
          getPage(url){
              let count = 0;
              axios({
                    method: 'get',
                    url: url,
                    headers: {"Content-Type": "application/json"},
                    })
                .then(response => {
                    this.searchResults = response.data.results;
                    this.next = response.data.next;
                    this.pre = response.data.previous;
                    this.searchStart = false;
                })
                .catch(error => {
                    this.errorMessage = error //'خطایی در گرفتن اطلاعات کاربر رخ داد'; //error.data
                    this.searchStart = false;
              });
            },
          getNext(){
            this.offset = (parseInt(this.next.split('=')[1]) - 1) * this.pageSize;
            console.log(this.next);
            this.getPage(this.next);
             
          },
          getPre(){
            let page = this.pre.split('=')[1];
            if (page){
              this.offset = (parseInt(page) - 1) * this.pageSize;
            }
            else{
              this.offset = 0;
            }
            this.getPage(this.pre);
          }
        },
        computed: {
          sname(){
            if (this.searchBy == 'sname'){
              return true;
            }
            return false;
          },
          spost(){
            if (this.searchBy == 'spost'){
              return true;
            }
            return false;
          },
        },
        created(){
          this.depList0();
          this.postList();
        },
   }
</script>

<template>
   <div class="flex flex-col items-center">
    <div class="text-xl text-gray-600 bg-gray-50 font-farsi font-bold hover:text-gray-900 
                  hover:ring-1 md:m-5 border-2 p-6 w-2/3" dir="rtl">
          
          <p class="mt-0 md:mb-5 text-lg text-gray-600 md:m-5 p-2 text-center">
              <span class="bg-red-50 py-2 px-6 font-farsi sm:text-2xs hover:text-gray-900 hover:ring-1">
                  محدوده جستجو
              </span>
          </p>
        <div class="md:grid  md:grid-cols-3 md:gap-4 flex flex-col font-farsi  items-center items-stretch">
          <DropDown label_title="واحد اصلی"  :options="mainDepOptions"
                            @onChangeValue="updateDep" :order=1 />
          <DropDown label_title="زیر واحد اصلی"  :options="mainSubDepOptions"
                            @onChangeValue="updateSubDep" :order=2 />
          <DropDown label_title="زیر واحد فرعی"  :options="subSubDepOptions"
                            @onChangeValue="updateSubSubDep" :order=3 />
        </div>
      </div>

      <div class="flex flex-col md:block items-center text-xl text-gray-600 bg-gray-50 font-farsi font-bold hover:text-gray-900 
                  hover:ring-1 m-5 border-2 p-6 w-2/3" dir="rtl">
          
          <p class="w-full mt-0 mb-5 items-center text-xs font-bold md:text-lg text-gray-600 m-5 p-2 text-center">
              <span v-if="sname" class="bg-red-50 py-2 px-6 font-farsi hover:text-gray-900 hover:ring-1">
                  قسمتی از نام یا فامیل را بنویسید
              </span>
               <span v-if="spost" class="bg-red-50 py-2 px-6 font-farsi hover:text-gray-900 hover:ring-1">
                  پست سازمانی را انتخاب کنید
              </span>
          </p>
        <div class="grid grid-cols-1 gap-4 font-farsi">

          <div class="flex">
              <div class="flex items-center mr-4">
                  <input id="inline-radio" type="radio" v-model="searchBy" value="sname" name="inline-radio-group" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                  <label for="inline-radio" class="mr-1 text-xs md:text-sm font-medium text-gray-900 dark:text-gray-300"> جستجو برحسب نام </label>
              </div>
              <div class="flex items-center mr-4">
                  <input id="inline-2-radio" type="radio" v-model="searchBy" value="spost" name="inline-radio-group" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                  <label for="inline-2-radio" class="mr-1 text-xs md:text-sm font-medium text-gray-900 dark:text-gray-300">جستجو برحسب پست سازمانی </label>
              </div>
          </div>

          <InputText  v-if="sname" v-model:value="family" @onChangeValue="updatefamily"
                          input_placeholder="نژادمحمدی" @onEnterKey="submitSearch"
                          :order=1 @onStateChange="updateErrorArray"/>
          <DropDown v-if="spost"  :options="searchPostOptions"
                            @onChangeValue="updateSearchPost" :order=5 @onEnterKey="submitSearch"/>

          <div class="flex justify-center">
              <button type="button" @click="submitSearch"
                  class="block w-1/2 mt-7 px-7 py-3 bg-blue-600 text-white font-medium text-sm 
                  leading-snug uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg 
                  focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 
                  active:shadow-lg transition duration-150 ease-in-out disabled:bg-gray-500">               
                  <svg v-if="searchStart" role="status" class="inline float-center w-4 h-4 mr-3 text-white animate-spin" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="#E5E7EB"/>
                  <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentColor"/>
                  </svg>
                  <span  v-if="!searchStart">
                    جستجو
                  </span>
              </button>
            </div>
        </div>
      </div>
      <TableResults :rows="searchResults" :offset="offset"/>
       <div class="flex flex-row items-center my-7">
            <!-- Previous Button -->
            <button v-if="next"  type="button" @click="getNext" class="inline-flex items-center py-2 px-4 mr-3 text-sm font-medium text-gray-500 bg-white rounded-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
              <svg class="mr-2 w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z" clip-rule="evenodd"></path></svg>
                بعدی
            </button>
            <button v-if="pre"  type="button" @click="getPre" class="inline-flex items-center py-2 px-4 text-sm font-medium text-gray-500 bg-white rounded-lg border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                قبلی
              <svg class="ml-2 w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
            </button>
        </div>
    </div>
      
</template>
