ckan.module('disclaimer', function (jQuery) {
  return {
    initialize() {
      const root = this.el.get(0)
      this.checkbox = root.querySelector('[type=checkbox]')
      if (!this.checkbox) return
      
      this.dep = document.querySelector(this.options.dep)
      this._updateState()
      root.addEventListener('change', this._onChange.bind(this))
      // this.el.on('change', jQuery.proxy(this._onChange, this))
    },
    _onChange(event) {
      this._updateState()
    },
    _updateState() {
      this.checked = this.checkbox.checked
      if (!this.checked) this.dep.setAttribute('disabled', 'true')
      else this.dep.removeAttribute('disabled')
    }
  }
})