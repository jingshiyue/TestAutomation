/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this file,
 * You can obtain one at http://mozilla.org/MPL/2.0/. */


function toArray(iter) {
    if (iter === null) {
        return null;
    }
    return Array.prototype.slice.call(iter);
}

function find(selector, elem) {
    if (!elem) {
        elem = document;
    }
    return elem.querySelector(selector);
}

function find_all(selector, elem) {
    if (!elem) {
        elem = document;
    }
    return toArray(elem.querySelectorAll(selector));
}

function sort_column(elem) {
    toggle_sort_states(elem);
    var colIndex = toArray(elem.parentNode.childNodes).indexOf(elem);
    var key;
    if (elem.classList.contains('numeric')) {
        key = key_num;
    } else if (elem.classList.contains('result')) {
        key = key_result;
    } else {
        key = key_alpha;
    }
    sort_table(elem, key(colIndex));
}

function show_all_extras() {
    find_all('.col-result').forEach(show_extras);
}

function hide_all_extras() {
    find_all('.col-result').forEach(hide_extras);
}

function show_extras(colresult_elem) {
    var extras = colresult_elem.parentNode.nextElementSibling;
    var expandcollapse = colresult_elem.firstElementChild;
    extras.classList.remove("collapsed");
    expandcollapse.classList.remove("expander");
    expandcollapse.classList.add("collapser");
}

function hide_extras(colresult_elem) {
    var extras = colresult_elem.parentNode.nextElementSibling;
    var expandcollapse = colresult_elem.firstElementChild;
    extras.classList.add("collapsed");
    expandcollapse.classList.remove("collapser");
    expandcollapse.classList.add("expander");
}

function show_filters() {
    var filter_items = document.getElementsByClassName('filter');
    for (var i = 0; i < filter_items.length; i++)
        filter_items[i].hidden = false;
}

function add_collapse() {
    // Add links for show/hide all
    var resulttable = find('table#results-table');
    var showhideall = document.createElement("p");
    showhideall.innerHTML = '<a href="javascript:show_all_extras()">Show all details</a> / ' +
                            '<a href="javascript:hide_all_extras()">Hide all details</a>';
    resulttable.parentElement.insertBefore(showhideall, resulttable);

    // Add show/hide link to each result
    find_all('.col-result').forEach(function(elem) {
        var collapsed = get_query_parameter('collapsed') || 'Passed';
        var extras = elem.parentNode.nextElementSibling;
        var expandcollapse = document.createElement("span");
        if (collapsed.includes(elem.innerHTML)) {
            extras.classList.add("collapsed");
            expandcollapse.classList.add("expander");
        } else {
            expandcollapse.classList.add("collapser");
        }
        elem.appendChild(expandcollapse);

        elem.addEventListener("click", function(event) {
            if (event.currentTarget.parentNode.nextElementSibling.classList.contains("collapsed")) {
                show_extras(event.currentTarget);
            } else {
                hide_extras(event.currentTarget);
            }
        });
    })
}

function get_query_parameter(name) {
    var match = RegExp('[?&]' + name + '=([^&]*)').exec(window.location.search);
    return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
}

function init () {
    reset_sort_headers();

    add_collapse();

    show_filters();

    toggle_sort_states(find('.initial-sort'));

    find_all('.sortable').forEach(function(elem) {
        elem.addEventListener("click",
                              function(event) {
                                  sort_column(elem);
                              }, false)
    });
	
	//mycode，
	var h1 = document.getElementsByTagName('h1')[0];
	var table = document.getElementById('environment')
	var td_list = table.getElementsByTagName("td")
	//更改项目名
	for(var i = 0; i < td_list.length; i++){
		if (td_list[i].innerText == "项目名称") {
			console.log(td_list[i+1].innerText)
			h1.innerText = td_list[i+1].innerText + "测试报告"
		}
	}
	//更改table中test一列内容
	var case_name_td = document.getElementsByClassName("col-name");
	for(var i = 0; i < case_name_td.length; i++){
		try{
			case_name_td[i].innerText = case_name_td[i].innerText.split("::")[1].substring(9,);
		}
		catch(err){
			console.log("没修改table中test一列内容")
		}
	}
	//修改table中Test Data和Description列的宽度
	var ths = document.getElementById("results-table-head").getElementsByTagName("th");
	for(var i = 0; i < ths.length; i++){
		if (ths[i].innerText == "Test Data") {
			ths[i].style.width = "30%"
		}
		if (ths[i].innerText == "Description") {
			ths[i].style.width = "40%"
			//console.log(ths[i])
		}
	}
	//替换p标签,并设置该p的颜色
	var tbodys = document.getElementById("results-table").getElementsByTagName("tbody");
	for(var i = 0; i < tbodys.length; i++){
		trs = tbodys[i].getElementsByTagName("tr");
    tds = trs[0].getElementsByTagName("td");
		try{ 
		  desc = tds[2].innerText;
		  tds[2].innerHTML = desc;
		  ps = tds[2].getElementsByTagName("p")
			for(var j = 0; j < ps.length; j++){
			  ps[j].setAttribute("style","color:#999")
			}
		} 
		catch(err){ 
			console.log("desc is null")
		} 
  }
};

function sort_table(clicked, key_func) {
    var rows = find_all('.results-table-row');
    var reversed = !clicked.classList.contains('asc');
    var sorted_rows = sort(rows, key_func, reversed);
    /* Whole table is removed here because browsers acts much slower
     * when appending existing elements.
     */
    var thead = document.getElementById("results-table-head");
    document.getElementById('results-table').remove();
    var parent = document.createElement("table");
    parent.id = "results-table";
    parent.appendChild(thead);
    sorted_rows.forEach(function(elem) {
        parent.appendChild(elem);
    });
    document.getElementsByTagName("BODY")[0].appendChild(parent);
}

function sort(items, key_func, reversed) {
    var sort_array = items.map(function(item, i) {
        return [key_func(item), i];
    });
    var multiplier = reversed ? -1 : 1;

    sort_array.sort(function(a, b) {
        var key_a = a[0];
        var key_b = b[0];
        return multiplier * (key_a >= key_b ? 1 : -1);
    });

    return sort_array.map(function(item) {
        var index = item[1];
        return items[index];
    });
}

function key_alpha(col_index) {
    return function(elem) {
        return elem.childNodes[1].childNodes[col_index].firstChild.data.toLowerCase();
    };
}

function key_num(col_index) {
    return function(elem) {
        return parseFloat(elem.childNodes[1].childNodes[col_index].firstChild.data);
    };
}

function key_result(col_index) {
    return function(elem) {
        var strings = ['Error', 'Failed', 'Rerun', 'XFailed', 'XPassed',
                       'Skipped', 'Passed'];
        return strings.indexOf(elem.childNodes[1].childNodes[col_index].firstChild.data);
    };
}

function reset_sort_headers() {
    find_all('.sort-icon').forEach(function(elem) {
        elem.parentNode.removeChild(elem);
    });
    find_all('.sortable').forEach(function(elem) {
        var icon = document.createElement("div");
        icon.className = "sort-icon";
        icon.textContent = "vvv";
        elem.insertBefore(icon, elem.firstChild);
        elem.classList.remove("desc", "active");
        elem.classList.add("asc", "inactive");
    });
}

function toggle_sort_states(elem) {
    //if active, toggle between asc and desc
    if (elem.classList.contains('active')) {
        elem.classList.toggle('asc');
        elem.classList.toggle('desc');
    }

    //if inactive, reset all other functions and add ascending active
    if (elem.classList.contains('inactive')) {
        reset_sort_headers();
        elem.classList.remove('inactive');
        elem.classList.add('active');
    }
}

function is_all_rows_hidden(value) {
  return value.hidden == false;
}

function filter_table(elem) {
    var outcome_att = "data-test-result";
    var outcome = elem.getAttribute(outcome_att);
    class_outcome = outcome + " results-table-row";
    var outcome_rows = document.getElementsByClassName(class_outcome);

    for(var i = 0; i < outcome_rows.length; i++){
        outcome_rows[i].hidden = !elem.checked;
    }

    var rows = find_all('.results-table-row').filter(is_all_rows_hidden);
    var all_rows_hidden = rows.length == 0 ? true : false;
    var not_found_message = document.getElementById("not-found-message");
    not_found_message.hidden = !all_rows_hidden;
}
