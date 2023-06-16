ckan.module('join-vars', function (jQuery) {
    return {
      initialize() {

        const root = this.el.get(0)

        this.bool = root.querySelectorAll("input[type='radio']")

        this.options = root.querySelectorAll("input[name='join_vars']")

        this.bool.forEach(element => {
            element.addEventListener('click', () => {
                if (element.value == "true") {
                    this.options.forEach(ele => {
                        ele.disabled = false
                    })
                } else {
                    this.options.forEach(ele => {
                        ele.disabled = true
                    })
                }
            })
        });

      }
    }
  })