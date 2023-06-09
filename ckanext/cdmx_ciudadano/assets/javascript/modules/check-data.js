ckan.module('check-data', function (jQuery) {
    return {
      initialize() {
        const root = this.el.get(0)

        this.li = root.querySelectorAll('.li')
        this.bloque = root.querySelectorAll('.bloque')

        console.log(this.li);
        console.log(this.bloque);

        this.li.forEach((element, i )=> {
            this.li[i].addEventListener('click', () => {
              console.log("algo");
                this.li.forEach((ele, j) => {
                    this.li[j].classList.remove('activo')
                    this.bloque[j].classList.remove('activo')
                })
                this.li[i].classList.add('activo')
                this.bloque[i].classList.add('activo')
            })
        });

      }
    }
  })