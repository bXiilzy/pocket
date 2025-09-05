from django.contrib import admin
from .models import Transaction

# Register your models here.
# part 4
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'amount', 'transaction_type_display', 'created_at', 'updated_at')
    list_filter = ('transaction_type', 'created_at', 'user')
    search_fields = ('name', 'description', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 25
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'name', 'description')
        }),
        ('Transaction Details', {
            'fields': ('amount', 'transaction_type')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def transaction_type_display(self, obj):
        """Display transaction type as Income/Expense instead of 1/-1"""
        return "Income" if obj.transaction_type == 1 else "Expense"
    transaction_type_display.short_description = 'Type'
    transaction_type_display.admin_order_field = 'transaction_type'

# Alternative simple registration (uncomment if you prefer basic admin)
# admin.site.register(Transaction)