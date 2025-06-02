const formatCurrencyToBRL = (value) => {
    return Number(value).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
};

const formatDateToDMY = (date) => {
    return dayjs(date).format('DD/MM/YYYY');
};
