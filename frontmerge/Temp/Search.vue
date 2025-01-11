<script>
export default {
  methods: {
    depList1(sdep) {
      axios({
        method: "get",
        url: serverUrl + "/tel/deps/?level=1" + "&super-dep=" + sdep,
      })
        .then((response) => {
          this.mainSubDepOptions = response.data;
        })
        .catch((error) => {
          this.errorMessage = error; //'خطایی در گرفتن اطلاعات کاربر رخ داد'; //error.data
        });
    },
    depList2(sdep) {
      axios({
        method: "get",
        url: serverUrl + "/tel/deps/?level=2" + "&super-dep=" + sdep,
      })
        .then((response) => {
          this.subSubDepOptions = response.data;
        })
        .catch((error) => {
          this.errorMessage = error; //'خطایی در گرفتن اطلاعات کاربر رخ داد'; //error.data
        });
    },
    updateDep(newValue) {
      if (newValue && newValue != "0") {
        this.mainDep = newValue;
        this.finalDep = newValue;
        this.mainSubDepOptions = this.depList1(this.finalDep);
      } else {
        this.mainDep = "";
        this.finalDep = "";
      }
    },
    updateSubDep(newValue) {
      if (newValue && newValue != "0") {
        this.subDep = newValue;
        this.finalDep = newValue;
        this.subSubDepOptions = this.depList2(this.finalDep);
      } else {
        this.subDep = "";
        this.updateDep(this.mainDep);
      }
    },
    updateSubSubDep(newValue) {
      if (newValue && newValue != "0") {
        this.subSubDep = newValue;
        this.finalDep = newValue;
      } else {
        this.subSubDep = "";
        this.updateSubDep(this.subDep);
      }
    },
    updateSearchPost(newValue) {
      if (newValue && newValue != "0") {
        this.finalPost = newValue;
      } else {
        this.finalPost = 0;
      }
    },
  },
};
</script>

<template>
  <div>
    <DropDown
      label_title="واحد اصلی"
      :options="mainDepOptions"
      @onChangeValue="updateDep"
      :order="1"
    />
    <DropDown
      label_title="زیر واحد اصلی"
      :options="mainSubDepOptions"
      @onChangeValue="updateSubDep"
      :order="2"
    />
    <DropDown
      label_title="زیر واحد فرعی"
      :options="subSubDepOptions"
      @onChangeValue="updateSubSubDep"
      :order="3"
    />
  </div>
</template>
