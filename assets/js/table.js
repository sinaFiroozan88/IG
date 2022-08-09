$(document).ready(function() {
    var table = $('#table1').DataTable( {
        dom: 'Bfrtip',
        stateSave: true,
         fixedHeader: {
            header: true,
            footer: true
        },
        scrollY:        300,
        scrollX:        true,
        scroller:       true,
        scrollCollapse: true,
        keys: true,

        fixedColumns:   {
            leftColumns: 1,
            rightColumns: 1
        },
        select:         true,

        lengthMenu: [
            [ 12, 24, 50, 100, -1 ],
            [ '12 rows', '24 rows', '50 rows', '100 rows', 'Show all' ]

        ],
        buttons: ['pageLength', 'copy', 'csv', 'excel', 'pdf',
            {
                extend: 'print',
                exportOptions: {
                    columns: ':visible'
                }
            },

            {
                extend: 'colvis',
                collectionLayout: 'string four-column',
                postfixButtons: [ 'colvisRestore' ],

            }, ],
            // }, ,'columnsToggle' ],
        colReorder: true,
        initComplete: function () {
            this.api().columns().every( function () {
                var column = this;
                var select = $('<select><option value=""></option></select>')
                    .appendTo( $(column.footer()).empty() )
                    .on( 'change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(
                            $(this).val()
                        );

                        column
                            .search( val ? '^'+val+'$' : '', true, false )
                            .draw();
                    } );

                column.data().unique().sort().each( function ( d, j ) {
                    select.append( '<option value="'+d+'">'+d+'</option>' )
                } );
            } );
        }
    } );
        $('#reset').click( function (e) {
        e.preventDefault();

        table.colReorder.reset();
    } );
} );

