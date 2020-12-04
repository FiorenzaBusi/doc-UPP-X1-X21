;(function(win) {
  win.EditOnGithubPlugin = {}


  function create(docBase, docEditBase, title) {
    title = title || 'Edit on github'
    docEditBase = docEditBase || docBase.replace(/\/blob\//, '/edit/')

    function editDoc(event, vm) {
      var found;
      mdUrl = vm.route.file

      var xhttp = new XMLHttpRequest(); // Chiamata per controllare se il file esiste
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 404) {
          console.log("NOT FOUND");
          found = false;
          console.log(found);
        }else if (this.readyState == 4 && this.status == 200){
          console.log("FOUND")
          found = true;
          console.log(found);
        }
      };
      xhttp.open("GET", mdUrl, false);
      xhttp.send();

      var docName = vm.route.file
      //docName = docName.replace('smeup-wiki/','')
      console.log(docName)

      if (docName) {
        if(found == false){
          docEditBase = docEditBase.replace('/edit/', '/new/')
          docName = "?filename=" + docName
        }else{
          docEditBase = docEditBase.replace('/new/', '/edit/')
        }
        var editLink = docEditBase + docName
        window.open(editLink)
        event.preventDefault()
        return false
      } else {
        return true
      }
    }

    win.EditOnGithubPlugin.editDoc = editDoc

    return function(hook, vm) {
      win.EditOnGithubPlugin.onClick = function(event) {
        EditOnGithubPlugin.editDoc(event, vm)
      }

      var header = [
        '<div>',
        '<p style="float: right"><a href="',
        docBase,
        '" target="_blank" onclick="EditOnGithubPlugin.onClick(event)"><img src="edit.png" style="margin-left:20px; width:25px; height:25px">',
        '</a></p>',
        '</div>'
      ].join('')

      hook.afterEach(function (html) {
        return header + html
      })
    }
  }

  win.EditOnGithubPlugin.create = create
}) (window)