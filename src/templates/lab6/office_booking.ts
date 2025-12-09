interface Tenant {
    id: number;
    login: string;
    username: string;
}

interface Office {
    id: number;
    is_booking: boolean;
    price: number;
    tenant: Tenant | null;
    title: string;
}

interface OfficeListResponse {
    office_list: Office[];
}

interface OfficeResponse {
    id: number;
    is_booking: boolean;
    price: number;
    tenant: Tenant | null;
    title: string;
}

interface JsonRpcRequest {
    jsonrpc: string;
    method: string;
    office_id?: number;
}

interface JsonRpcResponse<T = any> {
    jsonrpc: string;
    result?: T;
    error?: {
        code: number;
        message: string;
    };
}

class OfficeManager {
    private readonly url = '/lab6/api';

    async fetchOffices(): Promise<void> {
        try {
            const response = await this.makeRequest<OfficeListResponse>('info');
            this.renderOfficeList(response.result?.office_list || []);
        } catch (error) {
            console.error('Ошибка загрузки офисов:', error);
            alert('Не удалось загрузить список офисов');
        }
    }

    async bookOffice(officeId: number): Promise<void> {
        await this.handleOfficeAction('booking', officeId, 'Офис успешно забронирован');
    }

    async cancelOffice(officeId: number): Promise<void> {
        await this.handleOfficeAction('cancelation', officeId, 'Бронь офиса отменена');
    }

    private async handleOfficeAction(method: 'booking' | 'cancelation', officeId: number, successMessage?: string): Promise<void> {
        try {
            const response = await this.makeRequest<OfficeResponse>(method, { office_id: officeId });
            
            if (response.error) {
                this.handleError(response.error);
            } else {
                if (successMessage) {
                    // alert(successMessage); // Раскомментировать если нужны уведомления об успехе
                }
                await this.fetchOffices();
            }
        } catch (error) {
            console.error('Ошибка операции:', error);
            alert('Произошла ошибка при выполнении операции');
        }
    }

    private async makeRequest<T>(method: string, params?: object): Promise<JsonRpcResponse<T>> {
        const request: JsonRpcRequest = {
            jsonrpc: '2.0',
            method,
            ...params
        };

        const response = await fetch(this.url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(request)
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return response.json();
    }

    private handleError(error: { code: number; message: string }): void {
        const errorMessages: { [key: number]: string } = {
            1: 'Вы не авторизованы',
            2: 'Офис не найден или недоступен для бронирования',
            [-32601]: 'Метод не найден'
        };
        
        alert(errorMessages[error.code] || error.message || 'Произошла ошибка');
    }

    private renderOfficeList(offices: Office[]): void {
        const list = document.getElementById('office-list');
        if (!list) return;

        list.innerHTML = offices.map(office => `
            <li>
                <strong>${office.title}</strong> - ${office.price}р
                <br>
                Статус: ${office.is_booking ? 'Забронирован' : 'Свободен'}
                ${office.tenant ? `<br>Арендатор: ${office.tenant.username}` : ''}
                <div class="office-actions">
                    ${!office.is_booking ? 
                        `<button onclick="officeManager.bookOffice(${office.id})">Забронировать</button>` : 
                        `<button onclick="officeManager.cancelOffice(${office.id})">Отменить бронь</button>`
                    }
                </div>
            </li>
        `).join('');
    }
}

const officeManager = new OfficeManager();

document.addEventListener('DOMContentLoaded', () => {
    officeManager.fetchOffices();
});
