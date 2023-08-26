/*
desenvolvimento com o plug-in https://pdfmake.github.io/docs/0.1/document-definition-object/page/

*/

function downloadPdf() {
  const nf = document.getElementById("nf").value;
  const origem = document.getElementById("origem").value;
  const vc = document.getElementById("vc").value;
  const destino = document.getElementById("destino").value;

  var docDefinition = {
    pageSize: {
      width: 210,
      height: 88,
    },
    pageMargins: [0, 0, 0, 0],
    content: [
      {
        style: "tableExample",
        table: {
          widths: [95, 140],
          heights: 39,
          body: [
            [
              {
                text: [`NF: `, { text: nf, bold: true, fontSize: 15 }],
              },
              {
                text: [
                  { text: "Venda Casada: \n", fontSize: 9 },
                  { text: vc, bold: true, fontSize: 15 },
                ],
              },
            ],
            [
              {
                text: [
                  { text: "Origem: \n", fontSize: 10 },
                  { text: origem, bold: true, fontSize: 20 },
                ],
              },
              {
                text: [
                  { text: "Destino: \n", fontSize: 10 },
                  { text: destino, bold: true, fontSize: 20 },
                ],
              },
            ],
          ],
        },
      },
    ],

    styles: {
      tableExample: {
        //bold: true,
        // margin: [-20, 0],
        fontSize: 18,
      },
    },
  };
  pdfMake.createPdf(docDefinition).open();
}
