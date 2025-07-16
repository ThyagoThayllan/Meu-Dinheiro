const formatCurrencyToBRL = (value) => {
    const normalizedValue = value.replace(',', '.');

    return Number(normalizedValue).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
};

const formatDateToDMY = (date) => {
    return dayjs(date).format('DD/MM/YYYY');
};
